
import os
import time
import pickle
from tensorflow.keras import Model, models
import glob


from bdi_predict.ml_logic.params import LOCAL_REGISTRY_PATH


def save_model(model: Model = None,
               params: dict = None,
               metrics: dict = None) -> None:
    """
    persist trained model, params and metrics
    """

    timestamp = time.strftime("%Y%m%d-%H%M%S")

    if os.environ.get("MODEL_TARGET") == "mlflow":

            # retrieve mlflow env params
            mlflow_tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
            mlflow_experiment = os.environ.get("MLFLOW_EXPERIMENT")
            mlflow_model_name = os.environ.get("MLFLOW_MODEL_NAME")
            

            # configure mlflow
            mlflow.set_tracking_uri(mlflow_tracking_uri)
            mlflow.set_experiment(experiment_name=mlflow_experiment)
            

            with mlflow.start_run():

                # STEP 1: push parameters to mlflow
                
                if params is not None:
                    mlflow.log_params(params)
                

                # STEP 2: push metrics to mlflow
                
                if metrics is not None:
                    mlflow.log_metrics(metrics)
                

                # STEP 3: push model to mlflow
                
                if model is not None:

                    mlflow.keras.log_model(keras_model=model,
                                        artifact_path="model",
                                        keras_module="tensorflow.keras",
                                        registered_model_name=mlflow_model_name)
                
        
            print("data saved to mlflow")
           
            return None



    print("\nSaving model to local disk...")

    # save params
    if params is not None:
        params_path = os.path.join(LOCAL_REGISTRY_PATH, "params", timestamp + ".pickle")
        print(f"- params path: {params_path}")
        with open(params_path, "wb") as file:
            pickle.dump(params, file)

    # save metrics
    if metrics is not None:
        metrics_path = os.path.join(LOCAL_REGISTRY_PATH, "metrics", timestamp + ".pickle")
        print(f"- metrics path: {metrics_path}")
        with open(metrics_path, "wb") as file:
            pickle.dump(metrics, file)

    # save model
    if model is not None:
        model_path = os.path.join(LOCAL_REGISTRY_PATH, "models", timestamp)
        print(f"- model path: {model_path}")
        model.save(model_path)

    print("\ndata saved locally")

    return None


def load_model(save_copy_locally=False) -> Model:
    """
    load the latest saved model, return None if no model found
    """
    print("\nLoad model from local disk...")

    # get latest model version
    model_directory = os.path.join(LOCAL_REGISTRY_PATH, "models")

    results = glob.glob(f"{model_directory}/*")
    if len(results) == 0:
        return None

    model_path = sorted(results)[-1]
    print(f"- path: {model_path}")

    model = models.load_model(model_path)
    print("\nModel loaded from disk")

    return model
