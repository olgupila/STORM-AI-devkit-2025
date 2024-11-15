# Satellite Atmospheric Density and Space Atmospheric Weather Dataset (SADSAW)

## Download the Challenge Dataset
The full challenge problem dataset will be made available to participants on December 16, 2024.

Participants should note that algorithm inputs must be limited to the phenomenology and data formats present in the public training dataset, but utilizing additional phenomenology or data sources for model validation and development is allowed and encouraged. 

Also note that since these datasets are collected from real spacecraft, there may be short gaps in the data due to blackout periods and instrument error. Participants should take this into account when designing their algorithms to ensure successful submissions.

## Challenge Dataset Description

SADSAW consists of a public challenge dataset and a private evaluation dataset. The public challenge dataset contains astrometric data and space weather data. 

### Astrometric Data
The astrometric data contains the measured atmospheric density along the trajectories of multiple satellites, each of the satellites operating with different mission objectives and equipped with different propulsion capabilities. The data is provided at a minimum 1-hour temporal resolution, and consists of the orbital elements, geographic positions, and atmospheric density measures of satellites. The figure below shows a snapshot of example challenge data for a single satellite.

TODO: Replace image
![alt text](example_data.png)

A short description of each column header and description is provided below: 

TODO: Fix descriptions
| Column Header  | Description | 
| ------------- | ------------- | 
| time  | Start of the study period  | 
| density  | End of the study period  | 
| density_orbitmean  | Initiate drift  | 
| validity_flag  | Adjust drift  |
| altitude  | Initiate station-keeping  | 
| latitude  | Initiate station-keeping  | 
| longitude  | Initiate station-keeping  |


### Space Weather Data

In addition, the public challenge dataset contains collected information on amagnetic field, plasma, indices, particles, and several derived parameters provided by the NASA Goddard Space Flight Center. This information gives insight into atmospheric conditions. The figure below shows a snapshot of example challenge space weather data.

TODO: Replace image
![alt text](example_data.png)

TODO: fix headers, description-- insert OMNI data headers here
| Type Label  | Description |
| ------------- | ------------- |
| xrsa | Not station-keeping |
| xrsb | Station-keeping using chemical propulsion system |
| EK | Station-keeping using electric propulsion system |
| HK | Station-keeping using hybrid propulsion system |

## Evaluation Dataset 
The private evaluation dataset contains additional data that will be used to evaluate the performance of the participants' models. This private evaluation dataset consists of the trajectories and atmospheric density values of satellites not included in the public challenge dataset.
