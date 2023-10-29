"""
    This is the main script that will create the predictions on test data and save 
    a predictions file.
"""
import time
from pathlib import Path
import pickle

import utils

start_time = time.time()

# INPUT/OUTPUT PATHS WITHIN THE DOCKER CONTAINER
TRAINED_MODEL_DIR = Path('/trained_model/')
TEST_DATA_DIR = Path('/dataset/test_data/')
TEST_PREDS_FP = Path('/predictions/test_predictions.csv')


# Rest of configuration, specific to this submission
feature_cols = ['Eccentricity', 'Semimajor axis (km)', 'Inclination (deg)', 
                'RAAN (deg)', 'Argument of periapsis (deg)', 'True anomaly (deg)', 
                'Latitude (deg)', 'Longitude (deg)', 'Altitude (km)', 'J2k X (km)', 
                'J2k Y (km)', 'J2k Z (km)', 'J2k Vx (km/s)', 'J2k Vy (km/s)', 
                'J2k Vz (km/s)']
lag_steps = 5

test_data, updated_feature_cols = utils.tabularize_data(
    TEST_DATA_DIR, feature_cols, lag_steps=lag_steps)

# Load the trained models (don't use the utils module, use pickle)
model_EW = pickle.load(open(TRAINED_MODEL_DIR / 'model_EW.pkl', 'rb'))
model_NS = pickle.load(open(TRAINED_MODEL_DIR / 'model_NS.pkl', 'rb'))
le_EW = pickle.load(open(TRAINED_MODEL_DIR / 'le_EW.pkl', 'rb'))
le_NS = pickle.load(open(TRAINED_MODEL_DIR / 'le_NS.pkl', 'rb'))

# Make predictions on the test data for EW
test_data['Predicted_EW'] = le_EW.inverse_transform(
    model_EW.predict(test_data[updated_feature_cols])
)

# Make predictions on the test data for NS
test_data['Predicted_NS'] = le_NS.inverse_transform(
    model_NS.predict(test_data[updated_feature_cols])
)

# Print the first few rows of the test data with predictions for both EW and NS
test_results = utils.convert_classifier_output(test_data)
print(test_results.head())

# Save the test results to a csv file to be submitted to the challenge
test_results.to_csv(TEST_PREDS_FP, index=False)