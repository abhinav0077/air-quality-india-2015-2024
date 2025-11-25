# 🌍 Air Quality Data Analysis (India, 2015–2024)

Analyzing air quality data across major Indian cities from 2015 to 2024.  
This project demonstrates a **complete end-to-end data pipeline**, including **data cleaning, processing, visualization, trend analysis, and city-level insights**, aimed at showcasing skills for Data Analyst / Data Scientist roles.

---

## 📁 Project Structure

air-quality-data-2015-2024/
│
├── data/
│ ├── raw/ # Original CSV files
│ ├── cleaned/ # Cleaned data
│ └── processed/ # Processed outputs
│
├── visuals/ # Plots, graphs & dashboards
└── scripts/
├── clean_data.py
├── analyze_data.py
├── report_top_cities.py
├── pollutant_distribution.py
├── city_trend_analysis.py
├── correlation_matrix.py
├── yearly_summary.py
├── station_stats.py
└── combined_dashboard.py

yaml
Copy code

---

## 🛠 Tech Stack

- Python 3.10+  
- Pandas, NumPy, Matplotlib, Seaborn  
- Jupyter Notebook / VS Code  
- Git & GitHub

---

## 🚀 Key Features

- **Automated Data Cleaning:** Removes duplicates, fixes missing values, standardizes dates.  
- **Trend Analysis:** PM2.5 & PM10 trends for each city.  
- **City Pollution Reports:** Annual ranking of most polluted cities, improving/declining trends.  
- **Pollutant Distribution:** Histograms & KDE plots for major pollutants.  
- **Yearly Summaries:** Average pollutant levels, max/min AQI, top polluted cities.  
- **Correlation Heatmaps:** Relationships between pollutants.  
- **Station-Level Insights:** Missing data rates, averages, top polluted stations.  
- **Combined Dashboard:** Generates multiple visualizations at once.

---

## 📈 Key Visualizations

- PM2.5 & AQI Trends  
- Pollutant Distribution Histograms  
- Top Polluted Cities Charts  
- Correlation Heatmaps  
- Yearly AQI Summaries  
- Station-Level Performance Reports  

---

## 💡 Key Insights

- Delhi consistently ranks highest in PM2.5 levels.  
- Winter months show peak pollution across most cities.  
- Southern cities have comparatively lower pollution levels.  
- PM2.5 and PM10 are strongly correlated.  
- AQI improved slightly after the 2020 lockdown.  

---

## 📜 Installation & Usage

1. **Install dependencies**  
```bash
pip install pandas numpy matplotlib seaborn
Run cleaning script

bash
Copy code
python scripts/clean_data.py
Run analysis & visualization scripts

bash
Copy code
python scripts/analyze_data.py
python scripts/report_top_cities.py
python scripts/yearly_summary.py
python scripts/pollutant_distribution.py
python scripts/city_trend_analysis.py
python scripts/correlation_matrix.py
python scripts/station_stats.py
python scripts/combined_dashboard.py
🔮 Future Enhancements
Deploy interactive dashboards using Streamlit

Implement AQI forecasting & anomaly detection with ML

Interactive city comparison tools & live AQI API

👨‍💻 Author
Abhinav Verma
Aiming for roles in Data Analysis, Data Science & Python Development
