
# STORM-AI-Propagator

### Instructions to create a Miniconda virtual environment with the Orekit Python wrapper

Installation Instructions for Miniconda can be found here: https://docs.anaconda.com/miniconda/install/

1. **Create a virtual environment**:

   ```bash
   conda create -n orekit_venv_v12 python=3.8.20 anaconda
   ```

2. **Activate the virtual environment**:

   ```bash
   conda activate orekit_venv_v12
   ```

3. **Install required packages using conda**:

   - Install **Orekit** (version 12.1.2):
     ```bash
     conda install -c conda-forge orekit=12.1.2
     ```

   - Install **Pandas**:
     ```bash
     conda install -c conda-forge panda
     ```

   - Install **NumPy**:
     ```bash
     conda install -c anaconda numpy
     ```

   - Install **Python-dateutil**:
     ```bash
     conda install -c anaconda python-dateutil
     ```

   - Install **Matplotlib**:
     ```bash
     conda install -c conda-forge matplotlib
     ```

4. **Check package version**:

   To verify the version of Orekit installed, use the following command:

   ```bash
   pip show orekit
   ```


