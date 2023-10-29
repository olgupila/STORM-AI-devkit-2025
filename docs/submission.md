# Submission Tutorial
Participants will be submitting their trained algorithm with their  code/workflow to generation predictions into the competition platform, in the programming language they prefer. Here we provide Docker containers and example submissions for common Python and Matlab, but participants are allowed to submit with other custom containers too. The performance of their trained AI algorithm will then be evaluated against our internal test data and evaluation metric on our remote server. Once the evaluation is complete, the results are sent back to the live leaderboard on the challenge platform. This allows for the usage of a private test set, which helps with data privacy concerns and prevents data leakage.

## Docker submission
### Inputs
The predictions script **must** load data from the `/dataset/test`directory in the docker container.

> Note: `/dataset` is an absolute directory path, mounted on the root directory of the container. It is not a path relative to the current working directory.

The data, as for the training set, is stored in our remote server as separate files with the following directory structure:
```
/
├── dataset                  
    ├── test                
        ├── test1.csv            # Ephems for object with ID test1
        ├── test2.csv            # Ephems for object with ID test2
        └── ...
```

### Required outputs
Your submission has to generate predictions, and save them as a `.csv` file.

- The csv file should be saved to `/predictions/test_predictions.csv` in the docker container. Note that `/submission` is an absolute directory path, mounted on the root directory of the container. It is not a path relative to the current working directory.
- The output `csv` file shoud have four columns:
    - `ObjectID`
    - `TimeIndex`: Relative to the first observation of the object, i.e., row number in the ephems table. Starts in `0`.
    - `Direction`: `EW` (East-West) or `NS` (North-South)
    - `Node`: Node label. See more in the [dataset page](https://splid-devkit.readthedocs.io/en/latest/dataset.html)
    - `Type`: Node type. See more in the [dataset page](https://splid-devkit.readthedocs.io/en/latest/dataset.html)

Example of output `csv`:
```
ObjectID,TimeIndex,Direction,Node,Type
1,0,EW,SS,CK
1,75,EW,ID,NK
1,0,NS,SS,HK
1,115,NS,IK,EK
2,25,EW,SK,CK
2,45,NS,IK,EK
```

### Computational restrictions for submissions
TBD

## Creating your own Docker image for the submission
If you want to create your own Docker image for your submission instead of using one of the two provided for [Python](../baseline_submissions/ml_python/Dockerfile) and [Matlab](TBD) submissions (for example, because you're using a different language), here are some considerations to take into account.

### GPU compatibility
If you want to make use of the GPU resources that are on the cloud infrastructure, then you should use a docker image that contains Nvidia cuda, and cudnn drivers. for example, `nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04`

### Tips
1. Use `python -m pip install` instead of `pip install` for installing python libraries.

2. Set the `--no-cache-dir` argument when installing python libraries. This keeps docker images smaller.

    ```bash
    # Example
    python -m pip install --no-cache-dir pandas
    ```

3. After installing linux packages, delete the repository cache (this keeps docker images smaller)

    ```bash
    # Exammple of code to delete the apt package cache
    rm -rf /var/lib/apt/lists/*
    ```

4. Only install the bare minimum you need to run predictions. It will keep docker images smaller.
    - During the early stages, you will probably make use of a lot of libraries to perform exploratory analysis. E.g., for visualizing data, creating plots, and exporting images.
    - Do not install all of those libraries on your system onto the Docker image that you submit. 
        - E.g. there is probably no need to be installing `matplotlib` or `plotly` to make predictions.