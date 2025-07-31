import pandas
def split_dataset(dataset: pandas.DataFrame, rate: float) -> list:
    df_1 = dataset.sample(frac=rate)
    df_2 = dataset.drop(df_1.index)
    return [df_1, df_2]
