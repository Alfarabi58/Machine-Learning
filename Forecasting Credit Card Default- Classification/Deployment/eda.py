# Streamlit
import streamlit as st

# Pandas
import pandas as pd

# Visualisasi
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    # Membuat judul
    st.title('Credit Card Default')

    # Membuat sub judul
    st.subheader('Project Machine Learning')

    # Menambah Gambar dari url
    st.image('https://koala.sh/api/image/v2-5g6be-6z5wm.jpg?width=1344&height=768&dream')

    # Membuat caption
    st.caption("Source: BigQuery")

    # Buat deskripsi
    st.write('## Problem Statement')
    '''
        Dataset ini berfokus pada masalah default kartu kredit, yaitu situasi di mana pemegang kartu kredit 
        gagal melakukan pembayaran tepat waktu. Masalah ini memiliki konsekuensi keuangan serius baik bagi 
        perusahaan penerbit kartu kredit maupun bagi pemegang kartu. Fenomena default kartu kredit dapat 
        menjadi perhatian serius dalam industri keuangan karena dapat mengakibatkan kerugian finansial yang
        signifikan. Identifikasi pola atau faktor yang mempengaruhi default kartu kredit dapat 
        membantu perusahaan dan lembaga keuangan dalam pengambilan keputusan yang lebih baik terkait manajemen 
        risiko, penilaian kredit, dan pencegahan kerugian.
    '''
    st.write('## Objective')
    '''
    Mengidentifikasi pola atau faktor-faktor yang mempengaruhi default kartu kredit. Dengan memahami dan 
    menganalisis pola default credit card menggunakan machine learning diharapkan dapat ditemukan wawasan 
    yang dapat mendukung pengambilan keputusan yang lebih baik dalam industri keuangan.
    '''

    st.divider()

    # Menampilkan dataframe
    st.write('## Data')
    df= pd.read_csv('dataset_credit_card.csv')
    st.dataframe(df)
    ''' Data ini diambil dari bigquery '''

    st.divider()

    # Visualisasi
    st.write('## Exploratory Data Analysis')

    # Menampilkan chart

    # Visualisasi 1: Histogram Umur
    st.subheader('Histogram Umur Pemegang Kartu')
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=30, kde=True)
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Visualisasi 2: Pie Chart Jenis Kelamin
    st.subheader('Persebaran Jenis Kelamin Pemegang Kartu')
    gender_counts = df['sex'].value_counts()
    st.write(gender_counts)
    plt.figure(figsize=(8, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
    st.bar_chart(gender_counts)

    # Visualisasi 3: Bar Chart Default vs Non-Default
    st.subheader('Jumlah Default vs Non-Default')
    default_counts = df['default_payment_next_month'].value_counts()
    st.write(default_counts)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='default_payment_next_month', data=df)
    st.bar_chart(default_counts)

    # Visualisasi 4: Scatter Plot Limit Kredit vs Umur
    st.subheader('Scatter Plot Limit Kredit vs Umur')
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='limit_balance', y='age', data=df)
    scatter_plot = plt.gcf()
    st.pyplot(scatter_plot)

    # Visualisasi 5: Bar Chart Education Level vs Default
    st.subheader('Bar Chart Jumlah Default Berdasarkan Pendidikan')
    bar_data = df['education_level'].value_counts()
    st.bar_chart(bar_data)

if __name__ == '__main__':
    run()