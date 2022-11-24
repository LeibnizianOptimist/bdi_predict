import numpy as np
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import MinMaxScaler






    
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
    
    X_train = df_train
    y_train = df_train["Price"]
    

    X_test  = df_test
    y_test = df_test["Price"]
    
    Xy_train = (X_train, y_train)
    Xy_test = (X_test, y_test)
    
    
    return (Xy_train, Xy_test)

def min_max_scaler(Xy_tuple:tuple) -> np.ndarray:
    """
    MinMaxScale the features.
    """
    
    scaler = MinMaxScaler()
    
    X_scaled = scaler.fit_transform(Xy_tuple[0])
    
    return X_scaled
    
    
def construct_generator(Xy_tuple:tuple) -> TimeseriesGenerator:
    """
    Construct a TimeseriesGenerator from X,y values to create
    sequences necessary to fit a model.
    """
    
    X = Xy_tuple[0]
    y = Xy_tuple[1]
    
    generator = TimeseriesGenerator(X,
                                    y,
                                    length=7,
                                    batch_size=6,
                                    sampling_rate=1,
                                    stride=1)
    
    return generator
    
    
    
    

    
 

