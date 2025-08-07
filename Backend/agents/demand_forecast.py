from langchain_core.runnables import RunnableLambda
import pandas as pd
from prophet import Prophet

# For now, use local CSV as mock data
def forecast_func(inputs):
    # inputs = {"sku_id": "...", "store_id": "..."}
    df = pd.read_csv("data/m5_sample.csv")

    df = df.rename(columns={"date": "ds", "sales": "y"})

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    result = forecast[["ds", "yhat"]].tail(10).to_dict(orient="records")
    return {"forecast": result}

forecast_agent = RunnableLambda(forecast_func)
