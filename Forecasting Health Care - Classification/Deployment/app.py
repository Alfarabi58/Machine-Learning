import eda
import predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ['Exploratory Data Analysis', 'Predict Health Care'])

# Sidebar dengan pesan-pesan tentang kesehatan
st.sidebar.markdown('# Selamat datang di Platform Kesehatan')
st.sidebar.write('Temukan wawasan yang berharga tentang data kesehatan kami!')
    
st.sidebar.markdown('# Jelajahi Dunia Kesehatan')
st.sidebar.write('Temukan fakta-fakta menarik tentang dunia kesehatan di sini.')
    
st.sidebar.markdown('# Eksplorasi Data Kesehatan')
st.sidebar.write('Mari kita bersama-sama menganalisis data untuk meningkatkan pemahaman tentang kesehatan.')
    
st.sidebar.markdown('# Prediksi Kesehatan Anda')
st.sidebar.write('Cari tahu hasil prediksi kesehatan berdasarkan data yang Anda berikan.')
    
st.sidebar.markdown('# Kesehatan dalam Genggaman')
st.sidebar.write('Temukan informasi kesehatan yang bermanfaat dengan aplikasi kami.')
    
st.sidebar.markdown('# Mengungkap Rahasia Kesehatan')
st.sidebar.write('Sambutlah pengetahuan baru tentang data kesehatan melalui eksplorasi interaktif.')
    
st.sidebar.markdown('# Kesehatan Anda, Prioritas Kami')
st.sidebar.write('Mari kita telusuri data untuk meningkatkan pemahaman tentang perawatan kesehatan.')


if navigation == 'Exploratory Data Analysis' :
    eda.run()
else:
    predict.run()