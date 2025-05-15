import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 2️⃣ Data Loading & Exploration ---
try:
    covid_df = pd.read_csv("owid-covid-data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: owid-covid-data.csv not found. Please ensure it's in the correct directory.")
    exit()

print("\n--- 2️⃣ Data Loading & Exploration ---")
print("\nDataset shape:", covid_df.shape)
print("\nColumns:", covid_df.columns)
print("\nFirst few rows:\n", covid_df.head())
print("\nMissing values:\n", covid_df.isnull().sum())
print("\nData Types:\n", covid_df.dtypes)

# --- 3️⃣ Data Cleaning ---
print("\n--- 3️⃣ Data Cleaning ---")
countries_of_interest = ['Nigeria', 'USA', 'South Africa', 'Kenya', 'India']
covid_df_filtered = covid_df[covid_df['location'].isin(countries_of_interest)].copy() # Use .copy() to avoid SettingWithCopyWarning
covid_df_filtered.dropna(subset=['date'], inplace=True)
covid_df_filtered['date'] = pd.to_datetime(covid_df_filtered['date'])
covid_df_filtered.fillna(0, inplace=True) # Replace missing numeric values with 0
print("\nFiltered DataFrame shape:", covid_df_filtered.shape)
print("\nMissing values after cleaning:\n", covid_df_filtered.isnull().sum())

# --- 4️⃣ Exploratory Data Analysis (EDA) ---
print("\n--- 4️⃣ Exploratory Data Analysis (EDA) ---")

# Plot total cases over time
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = covid_df_filtered[covid_df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.title("Total COVID-19 Cases Over Time")
plt.legend()
plt.grid(True)
plt.savefig("total_cases_over_time.png")
plt.show()

# Plot total deaths over time
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = covid_df_filtered[covid_df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.title("Total COVID-19 Deaths Over Time")
plt.legend()
plt.grid(True)
plt.savefig("total_deaths_over_time.png")
plt.show()

# Compare daily new cases
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = covid_df_filtered[covid_df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'], label=country)
plt.xlabel("Date")
plt.ylabel("Daily New Cases")
plt.title("Daily New COVID-19 Cases")
plt.legend()
plt.grid(True)
plt.savefig("daily_new_cases.png")
plt.show()

# Calculate and plot death rate
covid_df_filtered['death_rate'] = covid_df_filtered['total_deaths'] / covid_df_filtered['total_cases']
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = covid_df_filtered[covid_df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)
plt.xlabel("Date")
plt.ylabel("Death Rate (total_deaths / total_cases)")
plt.title("COVID-19 Death Rate Over Time")
plt.legend()
plt.grid(True)
plt.savefig("death_rate_over_time.png")
plt.show()

# --- 5️⃣ Visualizing Vaccination Progress ---
print("\n--- 5️⃣ Visualizing Vaccination Progress ---")

# Plot cumulative vaccinations over time
plt.figure(figsize=(12, 6))
for country in countries_of_interest:
    country_data = covid_df_filtered[covid_df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.xlabel("Date")
plt.ylabel("Cumulative Vaccinations")
plt.title("COVID-19 Cumulative Vaccinations Over Time")
plt.legend()
plt.grid(True)
plt.savefig("cumulative_vaccinations.png")
plt.show()

# --- 6️⃣ Optional: Build a Choropleth Map ---
# This requires additional libraries (plotly) and may not work in all environments.
# To make this section runnable, you should install plotly: pip install plotly
try:
    import plotly.express as px
    print("\n--- 6️⃣ Optional: Build a Choropleth Map ---")
    latest_data = covid_df[covid_df['date'] == covid_df['date'].max()]
    fig = px.choropleth(latest_data, locations="iso_code", color="total_cases_per_million",
                        hover_name="location", color_continuous_scale=px.colors.sequential.Plasma,
                        title="Total COVID-19 Cases per Million (Latest Date)")
    fig.show()
except ImportError:
    print("\n--- 6️⃣ Optional: Build a Choropleth Map ---")
    print("Plotly is not installed. Choropleth map cannot be generated.")

# --- 7️⃣ Insights & Reporting ---
print("\n--- 7️⃣ Insights & Reporting ---")
print("\nKey Insights:")
print("- The total cases and deaths have generally increased over time in all three countries (Kenya, USA, and India), but the rate of increase varies.")
print("- The daily new cases show fluctuations, indicating waves of infections.")
print("- The death rate (total deaths / total cases) varies between countries and over time.")
print("- Vaccination campaigns have progressed over time, but the pace and coverage differ across countries.")
print("\nPlots have been saved as PNG files in the same directory.")