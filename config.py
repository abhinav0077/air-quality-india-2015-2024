"""
Configuration file for Air Quality Data Analysis Project
"""

import os

# Project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Data directories
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Output directories
VISUALS_DIR = os.path.join(PROJECT_ROOT, "visuals")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
NOTEBOOKS_DIR = os.path.join(PROJECT_ROOT, "notebooks")

# File paths
CITY_DAY_RAW = os.path.join(RAW_DATA_DIR, "city_day.csv")
CITY_HOUR_RAW = os.path.join(RAW_DATA_DIR, "city_hour.csv")
STATION_DAY_RAW = os.path.join(RAW_DATA_DIR, "station_day.csv")
STATION_HOUR_RAW = os.path.join(RAW_DATA_DIR, "station_hour.csv")
STATIONS_RAW = os.path.join(RAW_DATA_DIR, "stations.csv")

CITY_DAY_CLEANED = os.path.join(PROCESSED_DATA_DIR, "city_day_cleaned.csv")
CITY_HOUR_CLEANED = os.path.join(PROCESSED_DATA_DIR, "city_hour_cleaned.csv")
STATION_DAY_CLEANED = os.path.join(PROCESSED_DATA_DIR, "station_day_cleaned.csv")
STATION_HOUR_CLEANED = os.path.join(PROCESSED_DATA_DIR, "station_hour_cleaned.csv")
STATIONS_CLEANED = os.path.join(PROCESSED_DATA_DIR, "stations_cleaned.csv")

# Analysis parameters
POLLUTANTS = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']
DATE_COLUMNS = ["Date", "date", "timestamp", "Datetime", "DateTime", "DATE", "RecordedDate", "dt"]

# Visualization parameters
FIGURE_SIZE_TREND = (12, 6)
FIGURE_SIZE_HEATMAP = (14, 10)
FIGURE_SIZE_CORRELATION = (12, 10)

# AQI categories and colors
AQI_CATEGORIES = {
    'Good': {'range': (0, 50), 'color': 'green'},
    'Satisfactory': {'range': (51, 100), 'color': 'yellow'},
    'Moderate': {'range': (101, 200), 'color': 'orange'},
    'Poor': {'range': (201, 300), 'color': 'red'},
    'Very Poor': {'range': (301, 400), 'color': 'purple'},
    'Severe': {'range': (401, float('inf')), 'color': 'maroon'}
}

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Forecasting parameters
FORECAST_PERIOD = 365  # days
FORECAST_CONFIDENCE = 0.95

# Statistical test parameters
ANOVA_SIGNIFICANCE_LEVEL = 0.05

# Outlier detection parameters
IQR_MULTIPLIER = 1.5

# Missing value imputation methods
IMPUTATION_METHODS = {
    'numeric': 'interpolate',  # linear interpolation for time series
    'categorical': 'mode'
}
