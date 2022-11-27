from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
from bdi_predict.ml_logic.registry import load_model
from bdi_predict.ml_logic.params import LOCAL_REGISTRY_PATH
from datetime import datetime
import pytz


app = FastAPI()

app.state.model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/predict")
def predict(X1:float,
            X2:float,
            X3:float,
            X4:float,
            X5:float,
            X6:float,
            X7:float,
            X8:float,
            X9:float,
            X10:float
):
    """
    Type hniting is used to indicate the datatypes expected for the parameters of the functino 
    FastAPI uses this info in order to hand errors to the developpers providing incompatible parameters.
    FastAPI also provides variables of the expected datatype to use without type hinting we need to manually convert the 
    parameters of the functions which are all recieved as strings.
    """
    
    X = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]
    X_pred = np.array(X) 
    X_pred = X_pred.reshape(10, 1)
    assert X_pred.shape == (10, 1)
    
    model = app.state.model
    
    
    #The returned value of the model is the log difference between the previous input value and the next value (y_pred). We must utilise
    #We must utlise this predicted value to obtain a more useful number, an aboslute value of the index tomorrow, given the model. 
    
    y_pred_log_diff_100 = model.predict(X_pred)
    y_pred_log_diff_100 = float(y_pred_log_diff_100[0])
    
    #RECONVERSION TO THE LOG DIFFERENCE, y_pred_log_diff
    y_pred_log_diff = y_pred_log_diff_100/100
    
    
    #WORKING OUT COMMON LOG Y PRED, y_pred_log
    X10_log10 = np.log10(X10)
    y_pred_log = y_pred_log_diff + X10_log10
    
    #CONVERTING COMMON LOG y_pred_log to y_pred
    y_pred = 10**y_pred_log
    
    
    return {
        "BDI PREDICTION 1 WEEK INTO THE FUTRE": y_pred
    }


@app.get("/")
def root():
    return {
    'greetings': 'Welcome the BDI prediction interface.'
}
