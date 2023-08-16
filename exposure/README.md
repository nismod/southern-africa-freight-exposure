# Exposure analysis results

This folder contains outputs from the network exposure analysis.

The analysis is as follows:

1. split each network link into pieces along the lines of the hazard raster
   grids
2. assign the cell value of each hazard raster to each piece of link
3. filter out any zero or no-data exposure values

The split link-level exposure results are in each of the CSV files:

- `NO,FROMNODENO,TONODENO` columns are preserved from `Supply network_link.SHP`
- `split` runs from 0..n for each link, if this has been split into multiple parts
  along the grid/graticule of the hazard raster.
- `length_m` gives the length in metres of the split

### `exposure/Supply network_link.fathom.csv`

Exposure of network links to FATHOM flood hazard maps.

```
NO,FROMNODENO,TONODENO,split,length_m,rp,ssp,FU,P
42,58,81657,20,81,100,historical,0.09375,0.8656006
```

- `rp` - return period, in years
- `ssp` - shared socio-economic pathway (climate scenario), only historical
- `FU` - fluvial, undefended, flood depth in metres
- `P` - pluvial, flood depth in metres

### `exposure/Supply network_link.heat.csv`

Exposure of network links to extreme heat (Annual number of hot days, Tmax >
35/42/45 degrees), CMIP6 Mean Projections, Climatology, accessed through the
World Bank Group, Climate Change Knowledge Portal.

```
NO,FROMNODENO,TONODENO,split,length_m,epoch,quantile,ssp,hd35,hd42,hd45
1,1,2,0,191,1995-2014,p90,historical,0.7,0.0,0.0
```

- `epoch` - time period, one of 1995-2014 or 2040-2059
- `quantile` - percentile over distribution, one of median (50th), p10, p90
- `ssp` - shared socio-economic pathway (climate scenario), one of ssp119,
  ssp126, ssp245, ssp370, ssp585, historical
- `hd35` - Annual number of hot days, Tmax > 35 degrees
- `hd42` - Annual number of hot days, Tmax > 42 degrees
- `hd45` - Annual number of hot days, Tmax > 45 degrees

### `exposure/Supply network_link.storm.csv`

Exposure of network links to tropical cyclones, from Bloemendaal et al.

> Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts,
> J.C.J.H. (Jeroen) (2020): STORM tropical cyclone wind speed return periods.
> 4TU.ResearchData. Dataset. https://doi.org/10.4121/12705164.v3
>
> Bloemendaal, Nadia; de Moel, Hans; Dullaart, Job; Haarsma, R.J. (Reindert);
> Haigh, I.D. (Ivan); Martinez, Andrew B.; et al. (2022): STORM climate change
> tropical cyclone wind speed return periods. 4TU.ResearchData. Dataset.
> https://doi.org/10.4121/14510817.v3

```
NO,FROMNODENO,TONODENO,split,length_m,epoch,gcm,rp,cyclone
1,1,2,0,191,2050,CMCC-CM2-VHR4,1000,25.649797
```

- `epoch` - time period, one of historical or 2050
- `gcm` - constant, CMCC-CM2-VHR4, CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM
- `rp` - return period, in years
- `cyclone` - maximum wind speed in m/s, 10-minute average sustained wind speeds
  (U10)

## `exposure/Supply network_link.\*.parquet

These Parquet files contain the same data as above, in "wide" format with lots of columns.

Each file contains the common columns:

- 'NO', 'FROMNODENO', 'TONODENO', 'geometry', 'split'

And additional data columns, named in a way that encodes all the hazard details.
For example:

- 'epoch:1995-2014|hazard:hd35|quantile:median|ssp:historical'
- 'epoch:2040-2059|hazard:hd45|quantile:median|ssp:ssp245'

## `exposure/Supply network_link.\*.splits.gpkg

These GeoPackage files contain the only the "split" link data, in a common GIS format.

Each file contains the common columns:

- 'NO', 'FROMNODENO', 'TONODENO', 'split', 'geometry'
