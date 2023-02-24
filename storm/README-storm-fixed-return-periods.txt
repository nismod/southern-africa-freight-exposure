Global tropical cyclone wind speed return period maps.

This dataset is derived with minimal processing from the following datasets
created by Bloemendaal et al, which are released with a CC0 license:

[1] Bloemendaal, Nadia; de Moel, H. (Hans); Muis, S; Haigh, I.D. (Ivan); Aerts,
J.C.J.H. (Jeroen) (2020): STORM tropical cyclone wind speed return periods.
4TU.ResearchData. Dataset. https://doi.org/10.4121/12705164.v3

[2] Bloemendaal, Nadia; de Moel, Hans; Dullaart, Job; Haarsma, R.J. (Reindert);
Haigh, I.D. (Ivan); Martinez, Andrew B.; et al. (2022): STORM climate change
tropical cyclone wind speed return periods. 4TU.ResearchData. Dataset.
https://doi.org/10.4121/14510817.v3

Datasets containing tropical cyclone maximum wind speed (in m/s) return periods,
generated using the STORM datasets (see
https://www.nature.com/articles/s41597-020-0381-2) and STORM climate change
datasets (see https://figshare.com/s/397aff8631a7da2843fc). Return periods were
empirically calculated using Weibull's plotting formula. The
STORM_FIXED_RETURN_PERIOD dataset contains maximum wind speeds for a fixed set
of return periods at 10 km resolution in every basin and for every climate model
used here (see below).

The GeoTIFFs provided in the datasets linked above have been mosaiced into
single files with global extent for each climate model/return period using the
following code:

https://github.com/nismod/open-gira/blob/219315e57cba54bb18f033844cff5e48dd5979d7/workflow/rules/download/storm-ibtracs.smk#L126-L151

Files are named on the pattern:
STORM_FIXED_RETURN_PERIODS_{STORM_MODEL}_{STORM_RP}_YR_RP.tif

STORM_MODEL is be one of constant, CMCC-CM2-VHR4, CNRM-CM6-1-HR, EC-Earth3P-HR
or HadGEM3-GC31-HM. The "constant" files are for the present day, baseline
climate scenario as explained in dataset [1]. The other files are for 2050,
RCP8.5 under different models as explained in the paper linked from dataset [2].

STORM_RP is one of 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500,
600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000 or
10000.
