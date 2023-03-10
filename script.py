import pandas as pd
import numpy as np

def gender_tree(df):

    x = df['Sex']
    y = df['Survived']

    x_train = x == 'female'

    n_x = len(x)
    n_y = len(y)

    y_pred = x_train == y
    '''
    if its a female and survived y_pred = 1
    if its a female and died     y_pred = 0
    if its a male and survived   y_pred = 0 
    if its a male and died       y_pred = 1
    '''

    accuracy = sum(y_pred) / n_y
    #specificity = sum(y_pred==0) / n_y

    print(f'Accuracy: {accuracy*100}%')

def pre_processing(df):
    df['Age'].fillna(df['Age'].median(),  inplace=True)


def age_tree(

    
def main():
    df = pd.read_csv('data/train.csv')
    df_test = pd.read_csv('data/test.csv')
    
    gender_tree(df)
    #gender_tree(df_test)



    pass

if __name__ == '__main__':
    main()
