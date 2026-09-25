import pandas as pd
from src.energy_ml.features import add_calendar_features

def test_add_calendar_features():
    df = pd.DataFrame({"timestamp": ["2026-09-28 08:00:00", "2026-10-03 12:00:00"]})
    result = add_calendar_features(df)
    assert result["hour"].tolist() == [8, 12]
    assert result["day_of_week"].tolist() == [0, 5]
    assert result["is_weekend"].tolist() == [0, 1]
