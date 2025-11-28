import pandas as pd
import numpy as np
import os
from datetime import datetime

RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"

files = [
    "city_day.csv",
    "city_hour.csv",
    "station_day.csv",
    "station_hour.csv",
    "stations.csv"
]

def clean_file(filename):
    print(f"Cleaning {filename}...")
    df = pd.read_csv(RAW_PATH + filename)

    # Basic cleaning
    df = df.drop_duplicates()
    df = df.dropna(how='all')

    # Handle date columns
    date_cols = ['Date', 'Datetime']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df = df.dropna(subset=[col])
            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
            break

    # Handle numeric columns
    numeric_cols = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            # Fill missing values with median for pollutants
            if col in ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']:
                df[col] = df[col].fillna(df[col].median())
            # AQI should not be filled, keep as is

    # Handle categorical columns
    if 'AQI_Bucket' in df.columns:
        df['AQI_Bucket'] = df['AQI_Bucket'].astype('category')

    # Validate AQI ranges
    if 'AQI' in df.columns:
        df['AQI'] = df['AQI'].clip(0, 500)  # AQI max is 500

    # Sort by date if available
    if 'Date' in df.columns:
        df = df.sort_values('Date').reset_index(drop=True)
    elif 'Datetime' in df.columns:
        df = df.sort_values('Datetime').reset_index(drop=True)

    # Save cleaned file
    output_name = filename.replace(".csv", "_cleaned.csv")
    df.to_csv(PROCESSED_PATH + output_name, index=False)
    print(f"Saved cleaned file: {output_name}")

    # Generate summary
    summary = {
        'filename': output_name,
        'rows': len(df),
        'columns': len(df.columns),
        'date_range': f"{df.iloc[0]['Date'] if 'Date' in df.columns else df.iloc[0]['Datetime']} to {df.iloc[-1]['Date'] if 'Date' in df.columns else df.iloc[-1]['Datetime']}" if len(df) > 0 else 'N/A'
    }
    print(f"Summary: {summary}")

def main():
    for f in files:
        clean_file(f)

if __name__ == "__main__":
    main()
