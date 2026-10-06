def risk_segmentation(df):
    def risk(row):
        if row['RetentionScore'] > 0.7:
            return "Low Risk"
        elif row['RetentionScore'] > 0.4:
            return "Medium Risk"
        else:
            return "High Risk"

    df['RiskLevel'] = df.apply(risk, axis=1)
    return df