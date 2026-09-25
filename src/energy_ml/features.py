import pandas as pd

def add_calendar_features(df: pd.DataFrame, timestamp_col: str = "timestamp") -> pd.DataFrame:
    """Return a copy with basic calendar features extracted from a timestamp."""
    result = df.copy()
    ts = pd.to_datetime(result[timestamp_col])
    result["hour"] = ts.dt.hour
    result["day_of_week"] = ts.dt.dayofweek
    result["month"] = ts.dt.month
    result["is_weekend"] = (ts.dt.dayofweek >= 5).astype(int)
    return result
