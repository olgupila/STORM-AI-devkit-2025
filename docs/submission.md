# Submission Process

> The submission tutorial will be released to participants on **December 16, 2024**.

Once the competition phase begins on **December 16, 2024**, we will provide detailed instructions on the submission process. The competition will be hosted on the [EvalAI platform](https://eval.ai/), where you will need to register on the challenge's EvalAI webpage to submit your solutions. While we know you're eager to prepare your models, [here](https://evalai.readthedocs.io/en/latest/participate.html) are some general details to help you get started.

## Details on the Submission Process

Once the competition phase begins, participants will submit their trained algorithms, along with the associated code or workflows, to the competition platform. We will provide Docker containers and example submissions for Python, but you are welcome to use other programming languages by submitting custom containers.

To ensure submissions run smoothly and avoid dependency issues, all participants must include a `Dockerfile` and a `requirements.txt` file in their submission. To simplify the competition phase, we recommend start using Docker during the preparation of your solutions.

Each submission will be evaluated on our remote server using internal test data and a predefined evaluation metric. Once evaluated, results will be updated on the live leaderboard on the challenge platform.

![Process Image](_img/Submission_Process.png)

This approach ensures the use of a private test dataset, protecting data privacy and preventing data leakage.

## Important information

This is some information that you should take into account since now as will no change from now in the future.

### Computational restrictions for submissions
#### Hardware
The submission you make must take the following computational resource limits into consideration and not exceed them.

- **CPU** : 4 cpu cores will be available to you.
- **RAM** : Approx 16Gb of memory will be available.
- **GPU** : 1 GPU, with 16Gb of memory will be available.
- **Run Time** : Your submission should run within approx 10 minutes or less. If submissions take too long to run, they will fail.

#### Software
For maximum compatibility in Python-based submissions, it is recomended to use `python 3.10+``, and pin your python libraries to the following suggested versions (but only if you actually need those libraries).
```
scikit-learn==1.3.2
```
### Steps to create your own Docker image for the submission
> We will provide you with a `Dockerfile` in the baseline, so this part is **optional**. However, if you are not familiar with this tool, we recommend starting > with a very simple `Dockerfile` in your implementation. Below is a straightforward example, extracted from last year’s challenge:
>  ```Dockerfile
>     ####################################
>    # EXAMPLE IMAGE FOR PYTHON SUBMISSIONS
>    ####################################
>    FROM ubuntu:22.04
>
>    # Use this one for submissions that require GPU processing
>    #FROM nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04
>
>    RUN apt-get update && \
>        DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip && \
>        ln -sf /usr/bin/python3 /usr/bin/python && \
>        rm -rf /var/lib/apt/lists/*
>
>    # ADDITIONAL PYTHON DEPENDENCIES (if you have them)
>    COPY requirements.txt ./
>    RUN pip install -r requirements.txt
>
>    WORKDIR /app
>```

Here are some important considerations to keep in mind when creating your own `Dockerfile`.

#### GPU compatibility
If you want to make use of the GPU resources that are on the cloud infrastructure, then you should use a docker image that contains Nvidia cuda, and cudnn drivers. for example, `nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu22.04`. 

> Note: To use GPU in your container locally, you will need to install the [nvidia container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html). You will also need to use --gpus all flag with docker.

#### Tips
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

