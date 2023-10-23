# Usage
In this section, usage of the development toolkit is demonstrated via guided examples.

## Directory Structure
```
.
├── dataset                  # Contains the training dataset
│   ├── 1.csv                # Time series 1
│   ├── 2.csv                # Time series 2
│   └── ...                                     
├── labels                   # Contains the annotations for the training dataset
│   ├── 1.csv                # Annotations for time series 1
│   ├── 2.csv                # Annotations for time series 2
│   └── ...
├── outputs                  # Contains intermediate outputs for the helper functions 
└── example                  # Contains tutorial scripts

```

## Data Visualization
The following subsection guides the challengers in loading, manipulating, and visualizing the training data and labels.

To be updated.


## Heuristic-based Baseline
The following subsection guides the challengers in implementing a heuristic-based model. Readers are referred to the [baseline solutions page](https://splid-devkit.readthedocs.io/en/latest/baseline.html#heuristic-based-approach) for more information about this approach.

To be updated.

## Machine Learning-based Baseline
The following subsection guides the challengers in implementing a Random Forest classifier model. Readers are referred to the [baseline solutions page](https://splid-devkit.readthedocs.io/en/latest/baseline.html#machine-learning-based-approach) for more infomation of this approach.

### Preliminaries Notebook
The Preliminaries notebook serves as the initial step in setting up the challenge by preparing and structuring the dataset. It pulls in data from various directories specified under `config.data_dirs` and amalgamates them into a unified dataset. The notebook also handles the train-test split of this dataset, either based on a ratio or using predefined IDs.

**Configuration Parameters**:  
- `data_dirs`: List of directories containing the raw data.
- `test_ratio`: Proportion of the dataset to be used for testing.
- `test_ids`: Fixed test object IDs, omits the `test_ratio` parameter if provided.
- `output_dir`: Directory where the processed data is saved.
- `add_vcm_cols`: Boolean flag to add specific VCM columns.

### Baseline Model Notebook  
The Baseline Model notebook provides a foundational model using a Random Forest Classifier aimed at node detection. This notebook acts as a quick start guide and establishes a performance baseline for the challenge. It uses a predefined list of features for training the model and employs the `NodeDetectionEvaluator` for performance assessment.

**Configuration Parameters**:  
- `challenge_dir`: Directory containing the challenge data.
- `valid_ratio`: Proportion of the dataset to be used for validation.
- `lag_steps`: Number of lag steps for the model.
- `evaluation_tolerance`: Tolerance level used in the `NodeDetectionEvaluator`.

## Performance Evaluation
The `evaluation.py` script provides a standard way to assess the performance of the models submitted for the challenge. It employs metrics and evaluation techniques that are aligned with the challenge's objectives.

The toy datasets `ground_truth_toy.csv` and `participant_toy.csv` serve as simplified, example datasets for the challenge. These datasets are intended for initial testing and understanding of the evaluation script and the baseline model.

**Example Usage**
The `run_evaluator` function is the main entry point of the script and accepts the following arguments:

- `participant`: Path to the participant's CSV file.
- `ground_truth`: Path to the ground truth CSV file.
- `plot_object`: Object ID for which to plot evaluation details.

You can also run the script directly from the command line. For example:
```bash
python evaluation.py --participant=participant.csv --ground_truth=ground_truth.csv --plot_object=12345
```
This example assumes you have `participant.csv` and `ground_truth.csv` files in the expected directories, and you want to plot evaluation details for object ID `12345`. If no arguments are provided, the evaluation will be run for the toy datasets.

**Returns**
The `score` function within the file returns the evaluation metrics as per the challenge guidelines (that is, the F2 and the RMSE). Additionally, the precision and recall are also returned, and, if the `plot_object` parameter is provided, it generates plots for that specific object ID to aid in understanding the evaluation.
