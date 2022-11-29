import numpy as np
import pandas as pd
from tensorflow import keras
from keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import MinMaxScaler


def final_preprocess(df:pd.DataFrame) -> TimeseriesGenerator:
    """
    Function Objective: Obtain a set of X_predict values stored in a TimeseriesGenerator ready to be passed into our model.
    """
    
    
    def train_test_split(df:pd.DataFrame,
                        train_test_ratio: float,
                        input_length: int) -> tuple:
        """ 
        Returns a train dataframe and a test dataframe (df_train, df_test)
        from which one can sample (X,y) sequences using TimeseriesGenerator.
        df_train should contain all the timesteps until round(train_test_ratio * len(fold))   
        """
        

        # TRAIN SET

        last_train_idx = round(train_test_ratio * len(df))
        df_train = df.iloc[0:last_train_idx, :]

        # TEST SET

        first_test_idx = last_train_idx - input_length
        df_test = df.iloc[first_test_idx:, :]

        # CREATING X,Y FOR df_train AND df_test
        
        X_train = df_train[["Price", "CIP"]]
        y_train = df_train["log_diff"]
        

        X_test  = df_test[["Price", "CIP"]]
        y_test = df_test["log_diff"]
        
        Xy_train = (X_train, y_train)
        Xy_test = (X_test, y_test)
        
        
        return (Xy_train)

    def min_max_scaler_X(Xy_train:tuple) -> MinMaxScaler:
        """
        MinMaxScale X_inputs (FOR TRAINING AND TEST INPUTS ONLY)
        """
        
        scaler_X = MinMaxScaler()
        scaler_X.fit(Xy_train[0])
        
        #X_train_scaled = scaler_X.transform(Xy_train[0])
        #X_test_scaled = scaler_X.transform(Xy_test[0])
        
        return scaler_X
     
    def prediction_preprocessing(prediction_df:pd.DataFrame, scaler_X:MinMaxScaler) -> tuple:
        '''
        Function objective: Create a TimeseriesGenerator that will serve as the input to the model.predict() function that will called by the APi.
        '''
        X_input_prescaled = prediction_df[["Price", "CIP"]]
        X_input_scaled = scaler_X.transform(X_input_prescaled)
        
        y_true = np.array(prediction_df["log_diff"])

        predict_generator = TimeseriesGenerator(X_input_scaled, y_true, length=20, batch_size=1, sampling_rate=1, stride=1)
        

        return predict_generator
    
    #Actual running of the fuctions above:
    
    prediction_df = pd.DataFrame(df.tail(21))
    
    Xy_train = train_test_split(df=df, train_test_ratio=0.8, input_length=len(df))
    
    scaler_X = min_max_scaler_X(Xy_train=Xy_train)
    
    predict_generator = prediction_preprocessing(prediction_df,  scaler_X)
    
    X20 = prediction_df.iloc[20,2]
    
    return (predict_generator, X20)
    
        
    
    
    

    
 

