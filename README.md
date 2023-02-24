# Southern Africa Freight Model / Climate Hazard Exposure

This repository holds processing scripts for an exposure analysis of links in
a network model of major freight routes in Southern Africa.

Major steps in the process here:

- process hazard data
- intersect network links to find hazard (exposure) values for each link
- summarise the outputs by each exposed stretch of network link (filtering out
  zero-exposure stretches)
- summarise the outputs by admin-1 regions (applying a threshold to calculate
  the total network length exposed to each hazard under each scenario in each
  region)

Requirements

- Python >=3.8
- Python packages: geopandas pyarrow python-igraph rasterio shapely jupyter notebook
- GDAL command-line tools (gdal_translate, gdal_merge.py)
- GNU parallel

```bash
# install snail with specific version (or v0.3 when released)
pip install https://github.com/nismod/snail.git@148b861ac54595eceb2c83934d57b7d66fc3460b
```

## License

This codebase is made available under the MIT License, copyright (c) 2023 Tom
Russell and contributors. See [./LICENSE](./LICENSE) for details

## Acknowledgments

This project is done as part of the Climate Compatible Growth project, funded by
the UK Foreign Commonwealth and Development Office, in collaboration with the
World Bank.
