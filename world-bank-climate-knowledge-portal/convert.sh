# Convert NetCDF to GeoTIFF
find . -name '*hd35*.nc' | sed 's/.\///' | sed 's/.nc//' | parallel gdal_translate -a_srs EPSG:4326 NETCDF:{}.nc:climatology-hd35-annual-mean {}.tif
find . -name '*hd42*.nc' | sed 's/.\///' | sed 's/.nc//' | parallel gdal_translate -a_srs EPSG:4326 NETCDF:{}.nc:climatology-hd42-annual-mean {}.tif
find . -name '*hd45*.nc' | sed 's/.\///' | sed 's/.nc//' | parallel gdal_translate -a_srs EPSG:4326 NETCDF:{}.nc:climatology-hd45-annual-mean {}.tif
