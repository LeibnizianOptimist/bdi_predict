from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
import numpy as np
from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import MinMaxScaler

from bdi_predict.ml_logic.registry import load_model, load_data
from bdi_predict.ml_logic.params import LOCAL_REGISTRY_PATH
from bdi_predict.ml_logic.preprocessor import final_preprocess


app = FastAPI()

app.state.model = load_model()

app.state.data = load_data()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/predict")
def predict(
):
    """
    Type hinting is used to indicate the datatypes expected for the parameters of the functino 
    FastAPI uses this info in order to hand errors to the developpers providing incompatible parameters.
    FastAPI also provides variables of the expected datatype to use without type hinting we need to manually convert the 
    parameters of the functions which are all recieved as strings.
    """
    
    #Taking in data & model 
    df = app.state.data
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    
    model = app.state.model
    
    #Preprocess: Obtain prediction as a TimeseriesGenerator and y_true as a np.ndarray
    output = final_preprocess(df=df)
    
    #The returned value of the model is the log difference between the previous input value and the next value (y_pred). We must utilise
    #We must utlise this predicted value to obtain a more useful number, an aboslute value of the index tomorrow, given the model. 
    
    predict_generator = output[0]
    assert type(predict_generator) == TimeseriesGenerator
    
    X20_log = output[1]
    assert type(X20_log) == np.float64
     
    #Make prediction
    y_pred_log_diff = model.predict(predict_generator)
    assert type(y_pred_log_diff) == np.ndarray
    
    
    y_pred_log_diff = float(y_pred_log_diff[0][0])
    

    y_pred_log = y_pred_log_diff + X20_log
    
    #CONVERTING COMMON LOG y_pred_log to y_pred
    y_pred = 10**y_pred_log
    y_pred = float(y_pred)

    return {
        "BDI PREDICTION 1 DAY INTO THE FUTURE": y_pred
    }


@app.get("/")
def root():
    return {
    'greetings': 'Welcome the BDI prediction interface.'
}
