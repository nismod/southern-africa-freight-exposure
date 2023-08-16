import geopandas

for hazard in ("heat", "fathom", "storm"):
    print("Extracting", hazard)
    df = geopandas.read_parquet(f"exposure/Supply network_link.{hazard}.parquet")
    splits = df[["NO", "FROMNODENO", "TONODENO", "split", "geometry"]]
    splits.to_parquet(f"exposure/Supply network_link.{hazard}.splits.parquet")
    splits.to_file(f"exposure/Supply network_link.{hazard}.splits.gpkg")
print("Done.")
