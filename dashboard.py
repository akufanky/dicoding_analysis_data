import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_fix = pd.read_csv('hour.csv')

data_harian = data_fix.groupby('weekday')['cnt'].sum().reset_index()
label_data = {
    0: "Minggu",
    1: "Senin",
    2: "Selasa",
    3: "Rabu",
    4: "Kamis",
    5: "Jumat",
    6: "Sabtu"
}
data_harian['weekday'] = data_harian["weekday"].map(label_data)
data_harian = data_harian.sort_values('weekday', key=lambda x: x.map(label_data))

data_perjam = data_fix.groupby('hr')['cnt'].mean().reset_index()

st.title("Dashboard Sewa Sepeda")

st.subheader('Total Sewa Sepeda per Hari')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='weekday',
    y='cnt',
    data=data_harian,
    palette='viridis',
    ax=ax
)
ax.set_title('Total Sewa Sepeda per Hari')
ax.set_xlabel('Hari')
ax.set_ylabel('Total Penyewa')
st.pyplot(fig)

st.subheader('Rata - Rata Penyewa per Jam')
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(
    x='hr',
    y='cnt',
    data=data_perjam,
    marker='o',
    color='green',
    ax=ax
)
ax.set_title('Rata - Rata Penyewa per Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Rata - Rata Penyewa')
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)