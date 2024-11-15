# Dataset Information

## SADSAW Dataset

The Satellite Atmospheric Density and Space Atmospheric Weather (SADSAW) Dataset comprises of a public challenge and private evaluation dataset.

<b>The full public schallenge problem dataset will be made available to participants on December 16, 2024.</b>

### Challenge Dataset Description

SADSAW consists of a public challenge dataset and a private evaluation dataset. The public challenge dataset contains astrometric data and space weather data. 

#### Astrometric Data
The astrometric data contains the measured atmospheric density along the trajectories of multiple satellites, each of the satellites operating with different mission objectives and equipped with different propulsion capabilities. The data is provided at a minimum 1-hour temporal resolution, and consists of the orbital elements, geographic positions, and atmospheric density measures of satellites. The figure below shows a snapshot of example challenge data for a single satellite.

TODO: Replace image
![alt text](example_data.png)

A short description of each column header and description in the astrometric data is provided below: 

| Column Header  | Description | 
| ------------- | ------------- | 
| time  | Start of the study period  |
| semi_major_axis | Satellite semi-major axis. Defines the size of the orbit. Represented in | 
| eccentricity | Satellite eccentricity. Describes the shape of the orbit and how stretched it is. Ranges from 0 (perfectly circular) to 1 (parabolic); values greater than 1 indicate a hyperbolic orbit. Units in km for this dataset. | 
| inclination | Satellite inclination. The tilt of the orbit relative to the equatorial plane of the central body; the angle between the orbital plane and the equatorial plane. An inclination of 0° indicates an orbit in the equatorial plane, while 90° represents a polar orbit (crossing over the poles). Units in degrees. |
| right_ascension | Satellite right ascension of the ascending node. Defines horizontal orientation of the orbit; tilt of the orbit relative to the equatorial plane. Units in degrees. |
| arg_periapsis | Satellite argument of periapsis. Specifies the orientation of the orbit within its plane; defines where the orbit’s closest approach occurs within the plane of the orbit. Units in degrees. |
| true_anomaly | Satellite true anomaly. Position of the body along the orbit at a specific time. Units in degrees. |
| density |  Mass density of the atmosphere at satellite altitude; derived from satellite GPS accelerations. Used to calculate aerodynamic drag, which affects orbit decay and may require drift control adjustments. Units in kg/m^3.  |
| density_orbitmean  | Orbit-average of density derived from GPS accelerations. Helps assess long-term drag effects; used to decide if drift control maneuvers are needed due to accumulated orbital decay. Units in kg/m^3. | 
| validity_flag  | Indicator of data quality or reliability. Binary for this dataset; 0 for valid, 1 for invalid or unreliable. |
| altitude  | Satellite altitude. Units in km for this dataset.  | 
| latitude  | Satellite geodetic latitude. Units in degrees.   | 
| longitude  | Satellite geodetic longitude. Units in degrees. |
| local_solar_time | Local solar time at the satellite’s position relative to the Sun. Units in hours for this dataset. |


#### Space Weather Data

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

### Evaluation Dataset 
The private evaluation dataset contains additional data that will be used to evaluate the performance of the participants' models. This private evaluation dataset consists of the trajectories and atmospheric density values of satellites not included in the public challenge dataset.

## Guidelines

Participants should note that algorithm inputs must be limited to the phenomenology and data formats present in the public training dataset, but utilizing additional phenomenology or data sources for model validation and development is allowed and encouraged. 

Also note that since these datasets are collected from real spacecraft, there may be short gaps in the data due to blackout periods and instrument error. Participants should take this into account when designing their algorithms to ensure successful submissions.
