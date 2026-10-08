import pandas as pd
from pathlib import Path
def load_data(file_path):
    df=pd.read_csv(file_path)
    return df
def clean_data(df):
    df=df.drop(['CustomerId','Surname'],axis=1)
    df['HasCrCard']=df['HasCrCard'].astype(int)
    df['IsActiveMember']=df['IsActiveMember'].astype(int)
    df['Exited']=df['Exited'].astype(int)
    return df