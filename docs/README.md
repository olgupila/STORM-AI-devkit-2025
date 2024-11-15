<div align="center">

Welcome 
<h2> 2025 MIT ARCLab Competition for AI Innovation in Space </h2>

</div>

<!--
<p align="center">
  <a href="https://splid-devkit.readthedocs.io/en/latest/installation.html">Installation</a> •
  <a href="https://splid-devkit.readthedocs.io/en/latest/dataset.html">SPLID Dataset</a> •
  <a href="https://github.com/ARCLab-MIT/splid-devkit">Development Kit</a> •
  <a href="https://splid-devkit.readthedocs.io/en/latest/metric.html">Metric</a> <br>
  <a href="https://www.researchgate.net/publication/374083350_AI_SSA_Challenge_Problem_Satellite_Pattern-of-Life_Characterization_Dataset_and_Benchmark_Suite">Paper</a> •
  <a href="https://splid-devkit.readthedocs.io/en/latest/resources.html">Resources</a> •
  <a href="https://splid-devkit.readthedocs.io/en/latest/README.html">Documentation</a> •
  <a href="https://eval.ai/web/challenges/challenge-page/2164/overview">Challenge</a>
  
</p>

[![Python](https://img.shields.io/badge/python-%20%203.11-blue.svg)]()
[![Documentation Status](https://readthedocs.org/projects/splid-devkit/badge/?version=latest)](https://splid-devkit.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

______________________________________________________________________
<div align="left">
  
## Getting started
The Satellite Pattern-of-Life Identification Dataset (SPLID) can be downloaded from <a href="https://www.dropbox.com/scl/fo/jt5h1f82iycjb8elybmlz/h?rlkey=bjcmny486ddf7m0j7b9uok9ww&dl=0">here</a>. You can find installation instructions for the development toolkit (devkit) on the [installation page](https://splid-devkit.readthedocs.io/en/latest/installation.html), and detailed information about the dataset is available on the [dataset page](https://splid-devkit.readthedocs.io/en/latest/dataset.html).

For those interested in participating in the satellite pattern-of-life identification challenge, please refer to the competition [landing page](https://eval.ai/web/challenges/challenge-page/2164/overview) for complete details.

To get acquainted with the SPLID development toolkit, we recommend following these steps:
- <b>Read the SPLID Paper:</b> Start by reading the paper on the [Satellite Pattern-of-Life Characterization Dataset and Benchmark Suite](https://www.researchgate.net/publication/374083350_AI_SSA_Challenge_Problem_Satellite_Pattern-of-Life_Characterization_Dataset_and_Benchmark_Suite).
- <b>Explore Dataset Descriptions:</b> Review comprehensive descriptions of the [SPLID dataset](https://splid-devkit.readthedocs.io/en/latest/dataset.html) to understand its nuances.
- <b>Setup Toolkit and Dataset:</b> Follow the step-by-step instructions provided on the [installation page](https://splid-devkit.readthedocs.io/en/latest/installation.html) to set up the devkit and dataset.
- <b>Tutorials to Get Started:</b> We've prepared tutorials in the [baseline_submissions folder](https://github.com/ARCLab-MIT/splid-devkit/tree/main/baseline_submissions), each covering essential topics:
    - `data_visualization.ipynb`: This tutorial guides you on loading, manipulating, and visualizing the training data and labels.
    - `heuristic_baseline.ipynb`: Here, you'll find a tutorial demonstrating the baseline heuristic solution. It explains the heuristic approach, illustrates how performance is measured, and provides visualizations of the results.
    - `ml_baseline.ipynb`: This tutorial takes you through the development of the baseline machine learning solution. It describes the training workflow, showcases how performance is assessed, and offers visualizations of the results.

-->
______________________________________________________________________

<div align="center">

<h3>Competition Overview </h3>

</div>

<div align="left">

In 2024, solar storms have lit up the skies with stunning Auroras across the United States. But while these displays are captivating to observers on the ground, space weather has the potential to wreak havoc on our global satellite infrastructure. Geomagnetic storms cause rapid heating in Earth’s thermosphere, which can lead to more than a 10x increase in satellite drag in mere hours. In May 2024, the Gannon storm caused the largest mass migration of satellites in history and severely degraded satellite collision avoidance systems worldwide for multiple days (Parker and Linares, 2024). This challenge tackles the urgent need for more efficient and accurate tracking and orbit prediction capabilities for resident space objects in the increasingly crowded near-Earth environment. As space activities expand, the demand for advanced technologies to monitor and manage satellite behavior becomes paramount. 

The challenge objective is to develop cutting-edge AI algorithms for nowcasting and forecasting space weather-driven changes in atmospheric density across low earth orbit using historical space weather observations. The available phenomenology include solar and geomagnetic space weather indices,measurements of the interplanetary magnetic field, and measured solar wind parameters. Participants are provided with an existing empirical atmospheric density model and spacecraft accelerometer-derived in situ densities and are tasked with training or creating models to forecast the atmospheric density.

(Adapted from [Transformer-based Atmospheric Density Forecasting by Julia Briden, Peng Mun Siew, Victor Rodriguez-Fernandez, and Richard Linares](https://arxiv.org/abs/2310.16912))

</div>


______________________________________________________________________

<div align="center">
<h3> Dataset </h3>
</div>

<div align="left">

You can download the challenge dataset [here](https://www.dropbox.com/scl/fo/nz1j92xpr6eet3fa5mx5i/ADMYs2zfr3dvxJ-FFd5dmM8?rlkey=9k81cc7sk0v6g7pkyd2zyk4ae&st=fkzsu8bn&dl=0), and view our wiki page for more detailed information about the dataset and guidelines for using it [here](https://2025-ai-challenge.readthedocs.io/en/latest/dataset.html).

The Satellite Atmospheric Density and Space Atmospheric Weather Dataset (SADSAW) contains collected orbital elements and satellite atmospheric densities, as well as collected information on magnetic field, plasma, indices, particles, X-Ray flux, and additional derived parameters. All dataset information is provided or derived from collections by organizations including the ESA, NASA Goddard Space Flight Center, and NOAA. 

SADSAW consists of a public challenge dataset that can be used to train and develop AI algorithms and a private evaluation dataset of the same type and format.

Algorithm inputs must be limited to the phenomenology and data formats present in the public training dataset, but utilizing additional phenomenology or data sources for model validation and development is allowed and encouraged.

</div>

______________________________________________________________________

<div align="center">
<h3> Development Toolkit </h3>
</div>

Participants will gain access to our full development toolkit on GitHub on December 16, 2024.

The development kit is coded in Python and comprises a set of essential utility functions, tutorials, and baseline implementations to assist participants in getting started with the challenge problem. The tutorials will guide participants in data reading, understanding, parsing, manipulation, as well as training, evaluating, and submitting their ML algorithms to the competition platform.


______________________________________________________________________


<div align="center">
<h3> Citation </h3>
</div>

<div align="left">

The challenge SADSAW dataset contains multiple data sources and should be credited in accordance with the policies of each data provider linked in the [Dataset](https://2025-ai-challenge.readthedocs.io/en/latest/dataset.html) and [Resources](https://2025-ai-challenge.readthedocs.io/en/latest/resources.html) sections. 

If you reference the challenge problem, please use the following citation:
```
@article{Briden2023,
  year = {2023},
  month = Sept,
  author = {Julia Briden and Peng Mun Siew and Victor Rodriguez-Fernandez and Richard Linares},
  title = {Transformer-based Atmospheric Density Forecasting},
  journal = {Advanced Maui Optical and Space Surveillance (AMOS) Technologies Conference},
  note = {Free preprint available at [https://arxiv.org/abs/2310.16912](https://arxiv.org/abs/2310.16912)}
}
```
</div>

<!-- ______________________________________________________________________ -->

<div align="center">
<h3>Contact Us</h3>
</div>

<div align="left">

You can reach us at ai_challenge@mit.edu.
If you have any questions regarding the devkit upon its release, submit an issue to the Github repo.

</div>

______________________________________________________________________

<div align="center">
<h3>Acknowledgement</h3>
</div>

<div align="left">
Research was sponsored by the Department of the Air Force Artificial Intelligence Accelerator and was accomplished under Cooperative Agreement Number FA8750-19-2-1000. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the Department of the Air Force or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein.

© 2024 Massachusetts Institute of Technology.
</div>
