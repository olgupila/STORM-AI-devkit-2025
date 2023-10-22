# Installation
Here, the step-by-step instructions to install the devkit is provided.

## Install Python
If you do not have Python installed, please refer to the anaconda installation instructions [here](https://docs.anaconda.com/free/anaconda/install/index.html). The devkit is tested for Python 3.11 on Ubuntu and Mac OS.

## Download the Devkit
Download the devkit using the terminal and mvoe inside the folder:
```
cd && git clone https://github.com/XXXX/splid-devkit.git && cd splid-devkit
```
The above will download the files to your home directory. While you can change this to an arbitrary directory, the rest of our tutorials assume that you are using the home directory.

Install the required packages by running the following command:
```
pip install -r requirements.txt
```

## Download the dataset
The challenge dataset can be downloaded from [here](google drive link). Please store the downloaded dataset into the `~/SPLID_devkit/dataset folder`. Description of the dataset is available on the [SPLID dataset page](https://splid-devkit.readthedocs.io/en/latest/dataset.html).

