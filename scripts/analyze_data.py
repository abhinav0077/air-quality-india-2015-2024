import pandas as pd
import matplotlib.pyplot as plt
import os

CLEAN_PATH = "../data/processed/"
VIS_PATH = "../visuals/"

FILES = [
    "city_day_cleaned.csv",
    "city_hour_cleaned.csv",
    "station_day_cleaned.csv",
    "station_hour_cleaned.csv",
    "stations_cleaned.csv"
]

# Auto-detect date column names
POSSIBLE_DATE_COLUMNS = [
    "Date", "date", "timestamp", "Datetime", "DateTime", 
    "DATE", "RecordedDate", "dt"
]

def detect_date_column(df):
    for col in POSSIBLE_DATE_COLUMNS:
        if col in df.columns:
            return col
    return None

def analyze_file(filename):
    print(f"\n📌 Analyzing: {filename}")

    df = pd.read_csv(CLEAN_PATH + filename)

    print("Columns found:", df.columns.tolist())

    date_col = detect_date_column(df)

    if not date_col:
        print("❌ No date column found. Skipping time-based analysis.")
        return

    print(f"✅ Date column detected: {date_col}")

    # Convert date column
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col])

    # Only do PM2.5 trend if PM2.5 exists
    if "PM2.5" in df.columns:
        print("📊 Plotting PM2.5 trend…")

        daily_pm25 = df.groupby(date_col)["PM2.5"].mean()

        plt.figure(figsize=(10, 5))
        daily_pm25.plot()

        plt.title(f"Average PM2.5 Over Time ({filename})")
        plt.xlabel("Date")
        plt.ylabel("PM2.5")
        plt.tight_layout()

        out_path = VIS_PATH + filename.replace(".csv", "_pm25_trend.png")
        plt.savefig(out_path)
        plt.close()

        print(f"✅ Saved: {out_path}")
    else:
        print("⚠️ No PM2.5 column. Skipping PM2.5 analysis.")

def main():
    for f in FILES:
        analyze_file(f)

if __name__ == "__main__":
    main() 
