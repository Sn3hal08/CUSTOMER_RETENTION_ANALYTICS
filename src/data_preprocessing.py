import pandas as pd
def load_data(path):
    df=pd.read_csv("data/European_Bank.csv")
    return df
def clean_data(df):
    df=df.drop(['CustomerId','Surname'],axis=1)
    df['HasCrCard']=df['HasCrCard'].astype(int)
    df['IsActiveMember']=df['IsActiveMember'].astype(int)
    df['Exited']=df['Exited'].astype(int)
    return df