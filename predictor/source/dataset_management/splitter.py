import pandas

from definitions import GENERAL_SEED

def split_dataset(dataset: pandas.DataFrame, rate: float) -> list:
    df_1 = dataset.sample(frac=rate, random_state= GENERAL_SEED)
    df_2 = dataset.drop(df_1.index)
    return [df_1, df_2]
