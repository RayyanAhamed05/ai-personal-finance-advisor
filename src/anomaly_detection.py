import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    model = IsolationForest(contamination=0.1)

    df['anomaly'] = model.fit_predict(df[['amount']])

    anomalies = df[df['anomaly'] == -1]

    return anomalies

if __name__ == "__main__":

    df = pd.read_csv("data/finance_data.csv")

    anomalies = detect_anomalies(df)

    print("Unusual Expenses:")
    print(anomalies)