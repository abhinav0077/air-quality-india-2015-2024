# I created this script to clean the raw air quality data files.
# It handles duplicates, missing values, data types, and saves cleaned versions.

import pandas as pd
import numpy as np
import os
from datetime import datetime

# Paths to raw and processed data directories
RAW_PATH = "data/raw/"
PROCESSED_PATH = "data/processed/"

# List of files I need to clean
files = [
    "city_day.csv",
    "city_hour.csv",
    "station_day.csv",
    "station_hour.csv",
    "stations.csv"
]

def clean_file(filename):
    """
    Clean a single CSV file by handling duplicates, dates, numerics, and categories.
    I designed this function to standardize the data for analysis.
    """
    print(f"Cleaning {filename}...")
    df = pd.read_csv(RAW_PATH + filename)

    # Remove duplicate rows and empty rows
    df = df.drop_duplicates()
    df = df.dropna(how='all')

    # Convert date columns to datetime and standardize format
    date_cols = ['Date', 'Datetime']
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
            df = df.dropna(subset=[col])
            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
            break

    # Convert pollutant columns to numeric and fill missing values with median
    numeric_cols = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene', 'AQI']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            # For pollutants, I fill missing values with median to avoid skewing data
            if col in ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']:
                df[col] = df[col].fillna(df[col].median())

    # Convert AQI bucket to category type
    if 'AQI_Bucket' in df.columns:
        df['AQI_Bucket'] = df['AQI_Bucket'].astype('category')

    # Ensure AQI values are within valid range (0-500)
    if 'AQI' in df.columns:
        df['AQI'] = df['AQI'].clip(0, 500)

    # Sort data by date for chronological order
    if 'Date' in df.columns:
        df = df.sort_values('Date').reset_index(drop=True)
    elif 'Datetime' in df.columns:
        df = df.sort_values('Datetime').reset_index(drop=True)

    # Save the cleaned file with "_cleaned" suffix
    output_name = filename.replace(".csv", "_cleaned.csv")
    df.to_csv(PROCESSED_PATH + output_name, index=False)
    print(f"Saved cleaned file: {output_name}")

    # Print a summary of the cleaned data
    summary = {
        'filename': output_name,
        'rows': len(df),
        'columns': len(df.columns),
        'date_range': f"{df.iloc[0]['Date'] if 'Date' in df.columns else df.iloc[0]['Datetime']} to {df.iloc[-1]['Date'] if 'Date' in df.columns else df.iloc[-1]['Datetime']}" if len(df) > 0 else 'N/A'
    }
    print(f"Summary: {summary}")

def main():
    """Main function to clean all files in the list."""
    for f in files:
        clean_file(f)

if __name__ == "__main__":
    main()
