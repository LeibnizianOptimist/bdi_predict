from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from bdi_predict.ml_logic.registry import load_model
from bdi_predict.ml_logic.preprocessor import preprocess_features
from bdi_predict.main.main import pred
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
def predict(X): 
    # 1
    """
    we use type hinting to indicate the data types expected
    for the parameters of the function
    FastAPI uses this information in order to hand errors
    to the developpers providing incompatible parameters
    FastAPI also provides variables of the expected data type to use
    without type hinting we need to manually convert
    the parameters of the functions which are all received as strings
    """
    ## HOW TO IMPEMENT HTIS FOR UNIVARIATE VALUES? list containing a list: 
    
    
    model = app.state.model
    
    X_processed = preprocess_features(X)
    
    y_pred = model.predict(X_processed)
    
    y_pred = float(y_pred)
    
    return {
    'BDI predition value': y_pred
}


@app.get("/")
def root():
    return {
    'greeting': 'Welcome the BDI prediction interface.'
}
