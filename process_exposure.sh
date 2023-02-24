#!/bin/bash

snail -vv \
    process \
    -fs network.csv \
    -rs details_fathom.csv \
    -d .
mv network_shp/Supply\ network_link.SHP.processed.parquet exposure/Supply\ network_link.fathom.parquet

snail -vv \
    process \
    --features network.csv \
    --rasters details_heat.csv \
    --directory .
mv network_shp/Supply\ network_link.SHP.processed.parquet exposure/Supply\ network_link.heat.parquet

snail -vv \
    process \
    --features network.csv \
    --rasters details_storm.csv \
    --directory .
mv network_shp/Supply\ network_link.SHP.processed.parquet exposure/Supply\ network_link.storm.parquet

python summarise.py
