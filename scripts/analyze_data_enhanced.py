import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

def seasonal_anova_test(df, date_col, value_col, filename):
    """Perform ANOVA test for seasonal differences."""
    if date_col not in df.columns or value_col not in df.columns:
        logging.warning(f"Columns {date_col} or {value_col} not found. Skipping ANOVA.")
        return

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df['Season'] = df[date_col].dt.month % 12 // 3 + 1  # 1: Winter, 2: Spring, 3: Summer, 4: Fall
    df['Season'] = df['Season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})

    seasons = df['Season'].unique()
    if len(seasons) < 2:
        logging.info("Not enough seasons for ANOVA test.")
        return

    groups = [df[df['Season'] == season][value_col].dropna() for season in seasons]

    # ANOVA
    f_stat, p_value = stats.f_oneway(*groups)
    logging.info(f"ANOVA for {value_col} across seasons: F={f_stat:.2f}, p={p_value:.4f}")

    if p_value < 0.05:
        logging.info("Significant seasonal differences found.")
        # Post-hoc Tukey test
        tukey = pairwise_tukeyhsd(df[value_col], df['Season'])
        logging.info(f"Tukey HSD results:\n{tukey}")
    else:
        logging.info("No significant seasonal differences.")

def correlation_analysis(df, filename):
    """Perform correlation analysis on pollutants."""
    pollutants = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
    available_pollutants = [p for p in pollutants if p in df.columns]

    if len(available_pollutants) < 2:
        logging.warning("Not enough pollutants for correlation analysis.")
        return

    corr_matrix = df[available_pollutants].corr()

    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title(f"Pollutant Correlation Matrix ({filename})")
    plt.tight_layout()
    out_path = VIS_PATH + filename.replace(".csv", "_correlation.png")
    plt.savefig(out_path)
    plt.close()
    logging.info(f"Saved correlation heatmap: {out_path}")

def analyze_file(filename):
    logging.info(f"Analyzing: {filename}")

    df = pd.read_csv(CLEAN_PATH + filename)

    logging.info(f"Columns found: {df.columns.tolist()}")

    date_col = detect_date_column(df)

    if not date_col:
        logging.warning("No date column found. Skipping time-based analysis.")
        return

    logging.info(f"Date column detected: {date_col}")

    # Convert date column
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col])

    # PM2.5 trend
    if "PM2.5" in df.columns:
        logging.info("Plotting PM2.5 trend…")

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

        logging.info(f"Saved: {out_path}")

        # Seasonal ANOVA for PM2.5
        seasonal_anova_test(df, date_col, "PM2.5", filename)

    else:
        logging.warning("No PM2.5 column. Skipping PM2.5 analysis.")

    # Correlation analysis
    correlation_analysis(df, filename)

def main():
    for f in FILES:
        analyze_file(f)

if __name__ == "__main__":
    main()
