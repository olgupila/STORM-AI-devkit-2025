# Baseline solutions

A [baseline solution](https://github.com/ARCLab-MIT/2025-aichallenge-wiki/tree/main/baseline_solutions) will be made available to participants on December 16, 2024. 

This solution will help facilitate the assessment of more advanced AI solutions and help familiarize the participants with the dataset, methodologies, and evaluation pipeline. Participants who are new to the field can leverage the baseline implementation as a starting point and build upon the baseline implementation by iterating on the existing model and experimenting with modifications and incorporating newer AI techniques. 

In the meantime, we recommend that participants check out [the model this competition drew inspiration from](https://github.com/ARCLab-MIT/2025-aichallenge-devkit.git) to develop a deeper understanding of the atmospheric density forecasting problem.

We also provide participants with a possible solution below, to give an initial idea for their own solution design. 

## Example solution: pymsis
This solution draws inspiration from the model( ) that this challenge problem is based off of. We will use NRLMSIS 2.0, an empirical atmospheric density model.

NRLMSIS 2.0 takes in satellite time, altitude, longitude, latitude and two additional space weather parameters: F10.7 solar flux and Ap geomagnetic index. We source these space weather parameters from NASA's historical [OMNI dataset](https://omniweb.gsfc.nasa.gov/). 

We can then use the [pymsis](https://pypi.org/project/pymsis/) package to generate atmospheric density values along an expected satellite orbit. 



