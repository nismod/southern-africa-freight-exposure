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

## Acknowledgments

This project is done as part of the Climate Compatible Growth project, funded by
the UK Foreign Commonwealth and Development Office, in collaboration with the
World Bank.
