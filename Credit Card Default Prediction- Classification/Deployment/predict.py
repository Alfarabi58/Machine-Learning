import streamlit as st
import pandas as pd
import pickle

# Load model yang sudah dilatih
with open('best_svc.pkl', 'rb') as file_1:
    best_svc = pickle.load(file_1)

def run():
    # Streamlit UI
    st.title('Predict Credit Card Default')

    # Tampilkan form untuk input data
    with st.form('Predict Default'):
        st.subheader('Input Data Pemegang Kartu')

        # Kolom input data
        limit_balance = st.number_input('Limit Balance', min_value=0)
        st.subheader('Data Diri')
        sex = st.selectbox('Jenis Kelamin', options=['Male', 'Female'])
        education_level = st.selectbox('Pendidikan', options=['Graduate', 'Undergraduate', 'High School', 'Others', 'Unknown'])
        marital_status = st.selectbox('Status Pernikahan', options=['Single', 'Married', 'Divorced'])
        age = st.number_input('Usia Pemegang Kartu', min_value=18, max_value=100)
        st.divider()
        st.subheader('Pembayaran Ulang')
        pay_0 = st.slider('Pembayaran Ulang di September', min_value=-2, max_value=8)
        pay_2 = st.slider('Pembayaran Ulang di August', min_value=-2, max_value=8)
        pay_3 = st.slider('Pembayaran Ulang di July', min_value=-2, max_value=8)
        pay_4 = st.slider('Pembayaran Ulang di June', min_value=-2, max_value=8)
        pay_5 = st.slider('Pembayaran Ulang di Mei', min_value=-2, max_value=8)
        pay_6 = st.slider('Pembayaran Ulang di Apri', min_value=-2, max_value=8)
        st.divider()
        st.subheader('Tagihan')
        bill_amt1 = st.number_input('Tagihan Pada Bulan September', min_value=0)
        bill_amt2 = st.number_input('Tagihan Pada Bulan August', min_value=0)
        bill_amt3 = st.number_input('Tagihan Pada Bulan July', min_value=0)
        bill_amt4 = st.number_input('Tagihan Pada Bulan June', min_value=0)
        bill_amt5 = st.number_input('Tagihan Pada Bulan Mei', min_value=0)
        bill_amt6 = st.number_input('Tagihan Pada Bulan April', min_value=0)
        st.divider()
        st.subheader('Jumlah Pembayaran')
        pay_amt1 = st.number_input('Jumlah Pembayaran Terdahulu Pada September', min_value=0)
        pay_amt2 = st.number_input('Jumlah Pembayaran Terdahulu Pada August', min_value=0)
        pay_amt3 = st.number_input('Jumlah Pembayaran Terdahulu Pada July', min_value=0)
        pay_amt4 = st.number_input('Jumlah Pembayaran Terdahulu Pada June', min_value=0)
        pay_amt5 = st.number_input('Jumlah Pembayaran Terdahulu Pada Mei', min_value=0)
        pay_amt6 = st.number_input('Jumlah Pembayaran Terdahulu Pada April', min_value=0)

        # Tambahkan submit button sesuai kebutuhan
        submit_button = st.form_submit_button('Predict Default')

    if submit_button:
        # Lakukan prediksi menggunakan model
        df_inf = {
            'limit_balance': limit_balance,
            'sex': sex,
            'age': age,
            'education_level': education_level,
            'marital_status': marital_status,
            'pay_0': pay_0,
            'pay_2': pay_2,
            'pay_3': pay_3,
            'pay_4': pay_4,
            'pay_5': pay_5,
            'pay_6': pay_6,
            'bill_amt1': bill_amt1,
            'bill_amt2': bill_amt2,
            'bill_amt3': bill_amt3,
            'bill_amt4': bill_amt4,
            'bill_amt5': bill_amt5,
            'bill_amt6': bill_amt6,
            'pay_amt1': pay_amt1,
            'pay_amt2': pay_amt2,
            'pay_amt3': pay_amt3,
            'pay_amt4': pay_amt4,
            'pay_amt5': pay_amt5,
            'pay_amt6': pay_amt6
        }
        
        df_inf = pd.DataFrame([df_inf])
        prediction = best_svc.predict(df_inf)

        # Tampilkan hasil prediksi
        if prediction[0] == 0:
            st.error('Kartu Kredit Tidak Default')
        else:
            st.success('Kartu Kredit Default')

if __name__ == '__main__':
    run()
