import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul
st.title("DASHBOARD KUALITAS UDARA")

# Membaca dataset
data = pd.read_csv('cleaned_data.csv')

# Menampilkan data
st.subheader("Data Kualitas Udara")
st.write(data)

# Menghitung rata-rata O3 per jam
average_o3_per_hour = data.groupby('hour')['O3'].mean()

# Menampilkan jam dengan kadar O3 tertinggi
highest_o3_hour = average_o3_per_hour.idxmax()
highest_o3_value = average_o3_per_hour.max()
st.write(f"Jam dengan kadar O3 tertinggi adalah {highest_o3_hour} dengan nilai {highest_o3_value}.")

# Membuat visualisasi menggunakan grafik garis untuk O3
st.header("Rata-rata Kadar O3 per Jam")
plt.figure(figsize=(10, 6))
plt.plot(average_o3_per_hour.index, average_o3_per_hour.values, marker='o', linestyle='-', color='b')
plt.title('Rata-rata Kadar O3 per Jam')
plt.xlabel('Jam')
plt.ylabel('Rata-rata Kadar O3')
plt.xticks(rotation=0)
plt.grid()
st.pyplot(plt)  # Menampilkan grafik di Streamlit
plt.clf()  # Membersihkan figure untuk grafik berikutnya

# Menghitung rata-rata suhu (TEMP) pada bulan Februari
february_data = data[data['month'] == 2]  # Memfilter data
daily_avg_temp = february_data.groupby('day')['TEMP'].mean().reset_index()  # Menghitung rata-rata suhu harian

# Menghitung rata-rata suhu bulan Februari
average_temp_february = daily_avg_temp['TEMP'].mean()

# Menampilkan tabel rata-rata suhu harian di bulan Februari
st.write("Rata-rata suhu harian di bulan Februari:")
st.dataframe(daily_avg_temp)

# Membuat plot suhu harian di bulan Februari
st.header("Suhu Harian di Bulan Februari")
plt.figure(figsize=(10, 5))
plt.plot(daily_avg_temp['day'], daily_avg_temp['TEMP'], marker='o', label='Suhu Harian')
plt.axhline(y=average_temp_february, color='r', linestyle='--', label=f'Rata-rata Suhu ({average_temp_february:.2f}°C)')
plt.xlabel('Hari di Bulan Februari')
plt.ylabel('Suhu (°C)')
plt.title('Suhu Harian di Bulan Februari')
plt.xticks(daily_avg_temp['day'])  # Menampilkan semua hari di sumbu x
plt.legend()
plt.grid()
st.pyplot(plt)  # Menampilkan grafik di Streamlit