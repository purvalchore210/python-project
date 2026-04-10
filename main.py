import pandas as pd
import matplotlib.pyplot as plt
import calendar


df = pd.read_csv("weather.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Extract year & month
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


def categorize_temp(temp):
    if temp < 0:
        return "Freezing ❄️"
    elif temp <= 30:
        return "Normal 🌤️"
    else:
        return "Boiling 🔥"

df['category'] = df['temperature'].apply(categorize_temp)


monthly_avg = df.groupby('month')['temperature'].mean()

hottest_month = monthly_avg.idxmax()
coldest_month = monthly_avg.idxmin()

print("\n" + "="*40)
print("🌍 WEATHER DATA ANALYTICS DASHBOARD")
print("="*40)

print(f"\n🔥 Hottest Month: {calendar.month_name[hottest_month]} ({monthly_avg.max():.2f}°C)")
print(f"❄️ Coldest Month: {calendar.month_name[coldest_month]} ({monthly_avg.min():.2f}°C)")


print("\n📊 Temperature Category Distribution:\n")
print(df['category'].value_counts())

yearly_avg = df.groupby('year')['temperature'].mean()


plt.style.use('ggplot')
plt.figure(figsize=(12,6))

# Line Plot
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', linewidth=2)

# Fill Area
plt.fill_between(yearly_avg.index, yearly_avg.values, alpha=0.3)

# Highlight hottest & coldest year
max_year = yearly_avg.idxmax()
min_year = yearly_avg.idxmin()

plt.scatter(max_year, yearly_avg.max(), s=100, label="Hottest Year")
plt.scatter(min_year, yearly_avg.min(), s=100, label="Coldest Year")

# Labels & Title
plt.title("📈 10-Year Temperature Trend Analysis", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Average Temperature (°C)", fontsize=12)

plt.legend()
plt.grid(True)


plt.savefig("temperature_trend.png")


plt.show()


plt.figure(figsize=(12,6))

colors = df['temperature'].apply(lambda x: 'blue' if x < 0 else 'green' if x <= 30 else 'red')

plt.scatter(df['year'], df['temperature'], c=colors, alpha=0.6)

plt.title("🌡️ Temperature Category Visualization", fontsize=16)
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.savefig("temperature_categories.png")

plt.show()


print("\n✅ Analysis Complete! Graphs saved as images.")