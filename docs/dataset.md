# Satellite Atmospheric Density and Space Atmospheric Weather Dataset (SADSAW)

## Download the Challenge Dataset
The full challenge problem dataset will be made available to participants on December 16, 2024.

## Challenge Dataset Description
SADSAW consists of a public challenge dataset and a private evaluation dataset. The public challenge dataset contains the measured atmospheric density along the trajectories of multiple satellites, each of the satellites operating with different mission objectives and equipped with different propulsion capabilities. The astronometric data is provided at a minimum hourly temporal resolution, and consists of the orbital elements, geographic positions, and atmospheric density measures of satellites 

In addition, the public challenge dataset contains collected information on amagnetic field, plasma, indices, particles, and several derived parameters provided by the NASA Goddard Space Flight Center. This information gives insight into atmospheric conditions 

Algorithm inputs must be limited to the phenomenology and data formats present in the public training dataset, but utilizing additional phenomenology or data sources for model validation and development is allowed and encouraged.

The figure below shows a snapshot of example challenge data for a single satellite.

![alt text](example_data.png)

Each data is accompanied by a list of expert-annotated time-stamped pattern-of-life (PoL) nodes. Each row in the satellite PoL node list begins with a time index of the node, followed by the direction ("EW" for east-west and "NS" for north-south), the node type, and the propulsion type used while in this behavioral mode. The time index refers to the row index of the astrometric data that corresponds to that particular node. The description of each label is provided in the table below.

| Node Label  | Description | 
| ------------- | ------------- | 
| SS  | Start of the study period  | 
| ES  | End of the study period  | 
| ID  | Initiate drift  | 
| AD  | Adjust drift  |
| IK  | Initiate station-keeping  | 

| Type Label  | Description |
| ------------- | ------------- |
| NK | Not station-keeping |
| CK | Station-keeping using chemical propulsion system |
| EK | Station-keeping using electric propulsion system |
| HK | Station-keeping using hybrid propulsion system |

## Evaluation Dataset 
The private evaluation dataset contains additional data that will be used to evaluate the performance of the participants' models. This private evaluation dataset consists of the trajectories and atmospheric density values of satellites not included in the public challenge dataset.
