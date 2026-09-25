from pathlib import Path
import numpy as np
import pandas as pd

OUTPUT_PATH = Path("data/raw/sample_load.csv")

def main():
    rng = np.random.default_rng(42)
    timestamps = pd.date_range(start="2026-09-01 00:00:00", periods=24*30, freq="h")
    hour = timestamps.hour.to_numpy()
    dow = timestamps.dayofweek.to_numpy()
    weekend = (dow >= 5).astype(int)
    temperature = 8 + 6*np.sin((hour-14)/24*2*np.pi) + rng.normal(0, 2.0, len(timestamps))
    morning = 220*np.exp(-((hour-9)/3.0)**2)
    evening = 320*np.exp(-((hour-19)/3.5)**2)
    load = 1900 + morning + evening - 120*weekend - 18*temperature + rng.normal(0,45,len(timestamps))
    df = pd.DataFrame({
        "timestamp": timestamps,
        "temperature_c": np.round(temperature, 2),
        "is_weekend": weekend,
        "load_mw": np.round(load, 2),
    })
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
