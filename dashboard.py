import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur tema seaborn
sns.set_theme(style="whitegrid")

# Load Data (Pastikan main_data.csv ada di folder yang sama dengan file ini di GitHub)
# Jika di GitHub file main_data.csv ada di dalam folder 'dashboard', gunakan "dashboard/main_data.csv"
# Jika berdampingan langsung, gunakan "main_data.csv"
try:
    df = pd.read_csv("main_data.csv")
except:
    df = pd.read_csv("dashboard/main_data.csv")
    
df['dteday'] = pd.to_datetime(df['dteday'])

st.title("🚲 Bike Sharing Analysis Dashboard")

# Pertanyaan 1: Cuaca
st.subheader("1. Pengaruh Cuaca terhadap Penyewaan")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.barplot(x='weathersit', y='cnt', data=df, ax=ax1, palette='viridis', hue='weathersit', legend=False)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Total Penyewaan")
st.pyplot(fig1)
st.write("**Kesimpulan:** Cuaca cerah (Clear) meningkatkan minat penyewaan sepeda secara signifikan dibandingkan cuaca buruk.")

# Pertanyaan 2: Tren Bulanan
st.subheader("2. Tren Pertumbuhan Bulanan (2011-2012)")
df['month_year'] = df['dteday'].dt.to_period('M').astype(str)
monthly_df = df.groupby('month_year')['cnt'].sum().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_df, x='month_year', y='cnt', marker='o', ax=ax2, color='tab:blue', linewidth=2)
ax2.set_xlabel("Bulan - Tahun")
ax2.set_ylabel("Total Penyewaan")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)
st.write("**Kesimpulan:** Bisnis tumbuh pesat dari tahun 2011 ke 2012 dengan pola musiman yang jelas, di mana pertengahan tahun menjadi puncak penyewaan.")