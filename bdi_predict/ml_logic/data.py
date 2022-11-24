from taxifare.ml_logic.params import (COLUMN_NAMES_RAW,
                                            DTYPES_RAW_OPTIMIZED,
                                            DTYPES_RAW_OPTIMIZED_HEADLESS,
                                            DTYPES_PROCESSED_OPTIMIZED
                                            )

import os
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    clean raw data by removing buggy or irrelevant transactions
    or columns for the training set
    """

    # SETTING INDEX TO DATETIME
    
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    # RENAME COLUMNS
    df.rename(columns={"BDI_Price":"bdi",
                       "CSTEEL_Price":"CSTEEL",
                       ""
                       })
    
    print("\ndata cleaned")

    return df
