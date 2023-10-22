# Satellite Pattern-of-Life Identification Dataset (SPLID)

## Download the Dataset
The challenge dataset can be downloaded from [here](google drive link).

## Dataset Description
The SPLID dataset consists of a public challenge dataset and a private evaluation dataset. The public challenge dataset contains 500 simulated satellite trajectories, each operating under different mission objectives and equipped with different propulsion capabilities. The trajectories are generated using a high-fidelity astrodynamics simulator and are designed to represent a diverse set of satellite behaviors. The private evaluation dataset contains additional data that will be used to evaluate the performance of the participants' models. This private evaluation dataset consists of both simulated satellite trajectories and historical satellite trajectories generated from VCM data and high-accuracy ephemerides provided by satellite operators.

The dataset consists of astrometric data over six months at a two-hour temporal resolution. The astrometric data consists of the osculating orbital elements, geodetic positions, and the Cartesian states of the satellite in the J2000 inertial reference frame. The figure below shows a snapshot of the data for a single satellite.

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

Each data is accompanied by a list of expert-annotated time-stamped pattern-of-life (PoL) nodes. Each row in the satellite PoL node list begins with a time index of the node, followed by the direction (EW - east-west, NS - north-south), the node type, and the propulsion type used while in this behavioral mode. The time index refers to the row index of the astrometric data that corresponds to that particular node. The description of each label is provided in the table below.

<table>
  <tr>
    <th>Node Label</th>
    <th>Description</th> 
    <th>Type Label</th>
    <th>Description</th> 
  </tr>
  <tr>
    <td>SS</td>
    <td>Start of the study period</td> 
    <td>NK</td>
    <td>Not station-keeping</td>
  </tr>
  <tr>
    <td>ES</td>
    <td>End of the study period</td> 
    <td>CK</td>
    <td>Station-keeping using chemical propulsion system</td>
  </tr>
  <tr>
    <td>ID</td>
    <td>Initiate drift</td> 
    <td>EK</td>
    <td>Station-keeping using electric propulsion system</td>
  </tr>
  <tr>
    <td>AD</td>
    <td>Adjust drift</td> 
    <td>HK</td>
    <td>Station-keeping using hybrid propulsion system</td>
  </tr>
  <tr>
    <td>IK</td>
    <td>Initiate station-keeping</td> 
    <td> </td>
    <td> </td>
  </tr>
</table>