import pandas as pd
import numpy as np

def read_data(path='data/train.csv'):
    df = pd.read_csv(
            path,
            dtype=object,
            keep_default_na=True
            )
    return df

def preprocess(df):
    columns = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch',
               'Fare', 'Embarked']

    df = df[columns]

    df.replace(
            {
                'male': 1,
                'female': 2
            },
            inplace=True)

    df.replace(
            {
            'C': 1,
            'Q': 2,
            'S': 3,
            },
            inplace=True)

    df = df.astype(np.float64)
    return df

