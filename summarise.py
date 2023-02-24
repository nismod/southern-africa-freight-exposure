import geopandas
import pandas
from pyproj import Geod


def process_hazard(hazard, extract_regex, extract_colnames, threshold=1):
    geod = Geod(ellps="WGS84")
    wide_df = geopandas.read_parquet(f"exposure/Supply network_link.{hazard}.parquet")
    wide_df["length_m"] = wide_df.geometry.apply(geod.geometry_length).astype("int")

    # melt down to long dataframe, one row per hazard observation from single raster
    datacols = [c for c in wide_df.columns if ":" in c]
    keepcols = [
        "NO",
        "FROMNODENO",
        "TONODENO",
        "split",
        "length_m",
    ]
    melted = wide_df.melt(id_vars=keepcols, value_vars=datacols)
    hazard_params = melted.variable.str.extract(extract_regex)

    long_df = (
        pandas.concat([melted, hazard_params], axis=1)
        .drop("variable", axis=1)
        .query("value > 0")
    )
    # pivot back up to get "hazard" columns back, one row per epoch/ssp/rp...
    indexcols = keepcols + extract_colnames
    long_neat = long_df.pivot(
        index=indexcols,
        columns="hazard",
        values="value",
    ).fillna(0)

    # first summary output
    long_neat.to_csv(f"exposure/Supply network_link.{hazard}.csv")
    print(f"Wrote exposure/Supply network_link.{hazard}.csv")

    # create a region lookup
    lookup = wide_df[["NO", "geometry"]].drop_duplicates(subset="NO")
    adm1 = geopandas.read_file("gadm.gpkg")
    lookup_adm1 = geopandas.sjoin(lookup, adm1, how="left", predicate="intersects")[
        ["GID_0", "NAME_0", "GID_1", "NAME_1", "NO"]
    ].set_index("NO")

    # filter based on additional threshold
    above_threshold_df = (
        long_df.query(f"value > {threshold}")
        .set_index("NO")
        .join(lookup_adm1, how="left")
    )

    # pivot again to get hazard columns - now the values are "length_m above threshold"
    indexcols_summary = [
        "NO",
        "FROMNODENO",
        "TONODENO",
        "split",
        "GID_0",
        "NAME_0",
        "GID_1",
        "NAME_1",
    ] + extract_colnames
    above_threshold_df_neat = (
        above_threshold_df.reset_index()
        .pivot(
            index=indexcols_summary,
            columns="hazard",
            values="length_m",
        )
        .fillna(0)
    )

    # group by region
    groupby_cols = [
        "GID_0",
        "NAME_0",
        "GID_1",
        "NAME_1",
    ] + extract_colnames
    summary = (
        above_threshold_df_neat.reset_index()
        .drop(columns=["NO", "FROMNODENO", "TONODENO", "split"])
        .groupby(groupby_cols)
        .sum()
    )

    # second output - regional summary
    summary.to_csv(f"exposure/admin1.{hazard}.csv")
    print(f"Wrote exposure/admin1.{hazard}.csv")

    # pivot up to get one row per region
    summary_wide = (
        summary.reset_index()
        .pivot(
            index=[
                "GID_0",
                "NAME_0",
                "GID_1",
                "NAME_1",
            ],
            columns=extract_colnames,
        )
        .reset_index()
        .set_index("GID_1")
    )
    # fix up columns to be hacky strings again, not tuples, so we can write to GPKG
    newcols = []
    for c in summary_wide.columns:
        parts = [p for p in c if p != ""]
        newcols.append("_".join(parts))
    summary_wide.columns = newcols

    # join ADM1 regions
    summary_gdf = (
        adm1.set_index("GID_1")
        .join(summary_wide.drop(columns=["GID_0", "NAME_0", "NAME_1"]), how="left")
        .fillna(0)
    )
    summary_gdf.to_file(f"exposure/admin1.{hazard}.gpkg")
    print(f"Wrote exposure/admin1.{hazard}.gpkg")


if __name__ == "__main__":
    process_hazard(
        "storm",
        r"epoch:(?P<epoch>[^|]*)\|gcm:(?P<gcm>[^|]*)\|hazard:(?P<hazard>[^|]*)\|rp:(?P<rp>[^|]*)",
        ["epoch", "gcm", "rp"],
        14,  # m/s wind speed
    )
    process_hazard(
        "heat",
        r"epoch:(?P<epoch>[^|]*)\|hazard:(?P<hazard>[^|]*)\|quantile:(?P<quantile>[^|]*)\|ssp:(?P<ssp>[^|]*)",
        ["epoch", "quantile", "ssp"],
        1,  # days above hd threshold
    )
    process_hazard(
        "fathom",
        r"hazard:(?P<hazard>[^|]*)\|rp:(?P<rp>[^|]*)\|ssp:(?P<ssp>[^|]*)",
        ["rp", "ssp"],
        0.5,  # m flood depth
    )
