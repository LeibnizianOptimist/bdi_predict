from tensorflow.keras import Model, Sequential, layers

from tensorflow.keras.callbacks import EarlyStopping

from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.optimizers.schedules import ExponentialDecay

# FOR TYPE HINTS
from typing import Tuple
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator





def init_model() -> Model:
    
    """ 
    Initialize the LSTM Reucrrent Neural Network.
    """
    
    print("\nInitialising model...")
    model = Sequential()

    #LSTM LAYERS:
    
    model.add(layers.LSTM(400,
                          activation="tanh",
                          input_shape=(7,1),
                          return_sequences=False))

    #DENSE LAYERS:
    
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dense(1, activation="linear"))
    print("\nmodel initialized.")

    #SETTING UP OPTIMIZERS:
    
    lr_schedule = ExponentialDecay(initial_learning_rate=1e-3,
                                   decay_steps=10000,
                                   decay_rate=0.9)
    
    rmsprop = RMSprop(learning_rate=lr_schedule)
    
    #COMPILING MODEL:
    
    model.compile(loss="mse",
                  optimizer=rmsprop,
                  metrics="mae")
    print("\nmodel compiled.")
    

    return model




def train_model(model: Model,
                XandY:TimeseriesGenerator,
                patience=10,
                validation_data=TimeseriesGenerator) -> Tuple[Model]:
    
    """
    Fit model and return a the tuple (fitted_model, history)
    """
    
    print("\nTraining model...")
    
    #EarlyStopping DEFINITION:
    
    es = EarlyStopping(monitor="val_mae",
                       patience=patience,
                       restore_best_weights=True)
    
    #FITTING MODEL:
    
    history = model.fit(XandY,
                        epochs=100,
                        validation_data=validation_data,
                        shuffle=True,
                        callbacks=es)
    
    
    print(f"\nmodel trained ({len(XandY)} rows).")
     
    return model, history
    
    
    






