import eda
import predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ['EDA', 'Predict Credit Card Deafult'])

st.sidebar.markdown('# About')
st.sidebar.write('''Halaman Berikut Untuk Melihat Exploratory Data Analys dan Prediksi Credit Card Default''')

if navigation == 'EDA' :
    eda.run()
else:
    predict.run()