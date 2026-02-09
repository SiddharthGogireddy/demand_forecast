import joblib

model = joblib.load("demand_forecast_model.pkl")
columns = joblib.load("feature_columns.pkl")
