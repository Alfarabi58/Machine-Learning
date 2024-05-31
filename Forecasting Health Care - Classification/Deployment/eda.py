# Streamlit
import streamlit as st

# Pandas
import pandas as pd

# Visualisasi
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def run():
    # Membuat judul
    st.title('Health Care')

    # Membuat sub judul
    st.subheader('Project Machine Learning')

    st.divider()

    # Menambah Gambar dari url
    st.image('https://d2jx2rerrg6sh3.cloudfront.net/images/news/ImageForNews_746630_16826511086353889.jpg')

    # Membuat caption
    st.caption("Source: Google")

    st.divider()

    # Buat deskripsi
    st.write('## Problem Statement')
    st.write('''
        Sistem kesehatan modern menghasilkan sejumlah besar data yang berharga, mulai dari rekam medis elektronik hingga data asuransi dan biaya pengobatan. Data kesehatan ini mengandung wawasan yang penting untuk mengembangkan solusi yang dapat meningkatkan layanan kesehatan, mengoptimalkan biaya, dan meningkatkan hasil pasien. Oleh karena itu, analisis data kesehatan menjadi semakin penting dalam membantu mengidentifikasi tren kesehatan, mengelola risiko, dan mendukung pengambilan keputusan di industri kesehatan.
    ''')

    st.divider()

    st.write('## Objective')
    st.write('''
        Tujuan proyek ini adalah untuk mengembangkan model machine learning yang dapat memprediksi hasil tes medis (test results) berdasarkan informasi pasien yang tersedia dalam dataset kesehatan. 
    ''')

    st.divider()

    # Menampilkan dataframe
    st.write('## Data')
    df= pd.read_csv('healthcare_dataset.csv')
    st.dataframe(df)
    st.write('''Data ini diambil dari Kaggle (https://www.kaggle.com/datasets/prasad22/healthcare-dataset/code)''')

    st.divider()

    # Visualisasi
    st.write('## Exploratory Data Analysis')

    # Menampilkan chart

    # Visualisasi distribusi umur (Age)
    st.subheader('Distribution of Age')
    fig= plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=30, kde=True)
    st.pyplot(fig)
    st.write('''Dari histogram diatas menunjukan distribusi umur pasien, dari umur 20 tahun hingga lebih dari 80 tahun.''')
    
    st.divider()

    # Visualisasi distribusi jenis kelamin (Gender)
    st.subheader('Gender Distribution')
    gender_counts = df['Gender'].value_counts()
    fig = px.pie(gender_counts, values=gender_counts.values, names=gender_counts.index)
    st.plotly_chart(fig)
    st.write('''Dari pie chart diatas menunjukan bahwa pasien wanita (50.7%) sedikit lebih banyak dibanding pasien laki-laki (49.3%).''')

    st.divider()

    # Visualisasi distribusi tipe darah (Blood Type)
    st.subheader('Blood Type Distribution')
    blood_type_counts = df['Blood Type'].value_counts()
    st.bar_chart(blood_type_counts)
    st.write('''Dari bar chart diatas menunjukan distribusi macam-macam golongan darah pasien terbagi secara rata.''')

    st.divider()

    # Visualisasi distribusi kondisi medis (Medical Condition)
    st.subheader('Medical Condition Distribution')
    med_condition_counts = df['Medical Condition'].value_counts().nlargest(10)
    st.bar_chart(med_condition_counts)
    st.write('''Dari bar chart diatas menunjukan bahwa pasien yang memiliki penyakit asma dan kanker paling banyak, dan pasien yang memiliki penyakit diabetes dan obesitas paling sedikit.''')

    st.divider()

    # Visualisasi distribusi jenis masuk (Admission Type)
    st.subheader('Admission Type Distribution')
    admission_counts = df['Admission Type'].value_counts()
    fig = px.pie(admission_counts, values=admission_counts.values, names=admission_counts.index)
    st.plotly_chart(fig)
    st.write('''Dari pie chart diatas menunjukan distribusi jenis penerimaan pasien. pasien emergency (33.7%), pasien urgent (33.9%), dan pasien elective (32.4%).''')

    st.divider()

    # Visualisasi distribusi penyedia asuransi (Insurance Provider)
    st.subheader('Insurance Provider Distribution')
    insurance_counts = df['Insurance Provider'].value_counts().nlargest(10)
    st.bar_chart(insurance_counts)
    st.write('''Dari bar chart diatas menunjukan bahwa asuransi yang paling banyak digunakan oleh pasien yaitu cigma dan blue cross, sedangkan asuransi yang paling sedikit penggunanya yaitu mediacare.''')

    st.divider()

    # Visualisasi distribusi hasil tes (Test Results)
    st.subheader('Test Results Distribution')
    test_results_counts = df['Test Results'].value_counts()
    fig = px.pie(test_results_counts, values=test_results_counts.values, names=test_results_counts.index)
    st.plotly_chart(fig)
    st.write('''Dari pie chart diatas menunjukan hasil test pasien yang normal sebanyak 32.7%, pasien yang abnormal 34.6%, dan pasien yang inclonclusive sebanyak 32.8%.''')

if __name__ == '__main__':
    run()
