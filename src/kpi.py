def engagement_retention_ratio(df):
    active = df[df['IsActiveMember']==1]['Exited'].mean()
    inactive = df[df['IsActiveMember']==0]['Exited'].mean()
    return inactive / active


def product_depth(df):
    return df.groupby('NumOfProducts')['Exited'].mean()


def high_balance_risk(df):
    high = df[df['Balance'] > 100000]
    risk = high[high['IsActiveMember'] == 0]
    return risk['Exited'].mean()


def credit_card_stickiness(df):
    return df.groupby('HasCrCard')['Exited'].mean()