import mlflow
import sklearn.metrics as sk_m
from math import sqrt
import pickle
import os
import itertools
import pandas as pd


def get_experiment_id(experiment_name):
    experiment = None
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        experiment_id = mlflow.create_experiment(experiment_name)
    else:
        experiment_id = experiment.experiment_id
    mlflow.sklearn.autolog()
    return experiment_id

def set_mlflow_metrics(regressor, y_predicted = None, y_expected = None, mse = True, mae = True):
    mlflow.log_metric("iterations", regressor.n_iter_)
    if y_predicted is not None and y_expected is not None:
        if mse:
            # mlflow.log_metric("test_mse", sk_m.mean_squared_error(y_predicted, y_expected))
            sk_m.mean_squared_error(y_predicted, y_expected)
        if mae:
            # mlflow.log_metric("test_mae", sk_m.mean_absolute_error(y_predicted, y_expected))
            sk_m.mean_absolute_error(y_predicted, y_expected)

def get_scaler(run_id, scaler_name = 'scaler', loc_artifact_dir = "download_artifacts"):
    # if not os.path.exists(f"./{loc_artifact_dir:s}"):
        # os.mkdir(f"./{loc_artifact_dir:s}")
    local_path = mlflow.artifacts.download_artifacts(run_id = run_id)#, f'{scaler_name:s}', f"./{loc_artifact_dir:s}")
    with (open(local_path + f"/{scaler_name:s}" + f"/{scaler_name:s}.pkl", "rb") as scaler_file):      
        loaded_scaler = pickle.load(scaler_file)
    return loaded_scaler

def get_product_dict(**kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in itertools.product(*vals):
        yield dict(zip(keys, instance))

def get_data(preprocessing = 'direct', pcb_variations = False):
    '''
    Load data from a specified directory.
    preprocessing - You can choose from 3 different preprocessing methods: [direct, rectangular, ring]
    pcb_variations:
        False > Only variations of the decoupling capacitors are loaded
        True > Additionally, variations of the PCB geometry, material are inlcuded to the decap variations
    the data is returned as a pandas data frame
    '''

    if preprocessing.lower() == 'direct':
        file_name = "direct_preproc_decap.csv"
    elif preprocessing.lower() == 'ring':
        file_name = "ring_preproc_decap.csv"
    elif preprocessing.lower() == 'rectangular':
        file_name = "rectangular_preproc_decap.csv"
    else:
        print("Specify one of the following preprocessings: [direct, rectangular, ring]\nData loading termination!")
        return -1

    data_frame = pd.read_csv("data/" + file_name, index_col='simu_index')

    if not pcb_variations:
        data_frame = data_frame.drop(data_frame[data_frame["diel_height_y"] != 4.4].index)
        data_frame = data_frame.drop(data_frame[data_frame["epsilon_r_y"] != 4.2].index)
        data_frame = data_frame.drop(["diel_height_y", "epsilon_r_y"], axis = 1)

    return data_frame