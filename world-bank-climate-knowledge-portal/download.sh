# Download future climatology
for variable in "hd35" "hd42" "hd45"
do
for stat in "median" "p10" "p90"
do
for ssp in "ssp119" "ssp126" "ssp245" "ssp370" "ssp585"
do

    echo "wget \"https://climatedata.worldbank.org/thredds/fileServer/CRM/cmip6/all-regridded-bct-${ssp}-climatology/${variable}/${stat}/annual/climatology-${variable}-annual-mean/2040-2059/climatology-${variable}-annual-mean_cmip6_annual_all-regridded-bct-${ssp}-climatology_${stat}_2040-2059.nc\" \
        -O \"climatology-${variable}-annual-mean_cmip6_annual_all-regridded-bct-${ssp}-climatology_${stat}_2040-2059.nc\"" >> get_all.sh
done
done
done

# Download historical (no SSP needed)
for variable in "hd35" "hd42" "hd45"
do
for stat in "median" "p10" "p90"
do

    echo "wget \"https://climatedata.worldbank.org/thredds/fileServer/CRM/cmip6/all-regridded-bct-historical-climatology/${variable}/${stat}/annual/climatology-${variable}-annual-mean/1995-2014/climatology-${variable}-annual-mean_cmip6_annual_all-regridded-bct-historical-climatology_${stat}_1995-2014.nc\" \
        -O \"climatology-${variable}-annual-mean_cmip6_annual_all-regridded-bct-historical-climatology_${stat}_1995-2014.nc\"" >> get_all.sh
done
done

cat get_all.sh | parallel
