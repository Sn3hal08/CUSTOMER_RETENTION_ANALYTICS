def add_features(df):
    df['EngagementScore']=(
        df['IsActiveMember']*2+
        df['NumOfProducts']+
        df['HasCrCard']
    )

    def segment(row):
        if row['IsActiveMember']==1 and row['NumOfProducts']>=2:
            return "Highly Engaged"
        elif row['IsActiveMember']==0 and row['Balance']>100000:
            return "High Value At Risk"
        elif row['IsActiveMember']==1:
            return "Moderate"
        else:
            return "Low Engagement"

    df['Segment']=df.apply(segment,axis=1)
    df['RetentionScore']=(
        df['IsActiveMember']*0.4+
        df['NumOfProducts']*0.3+
        (df['Tenure']/df['Tenure'].max())*0.3
    )
    return df