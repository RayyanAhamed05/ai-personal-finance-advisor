from prophet import Prophet
import pandas as pd

def forecast_expenses(df_exp):

    # Monthly total expenses
    monthly = df_exp.groupby(
        df_exp['date'].dt.to_period('M')
    )['amount'].sum().reset_index()

    # Convert format for Prophet
    monthly['date'] = monthly['date'].dt.to_timestamp()

    prophet_df = monthly.rename(columns={
        'date': 'ds',
        'amount': 'y'
    })

    # Train model
    model = Prophet()
    model.fit(prophet_df)

    # Future prediction
    future = model.make_future_dataframe(periods=3, freq='ME')

    forecast = model.predict(future)

    return model, forecast