from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    X = df[['CreditScore','Balance','NumOfProducts','IsActiveMember']]
    y = df['Exited']

    model = RandomForestClassifier()
    model.fit(X, y)

    return model