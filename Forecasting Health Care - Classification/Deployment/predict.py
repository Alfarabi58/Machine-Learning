# Import Libraries
import streamlit as st
import pandas as pd
import pickle

# Load model yang sudah dilatih
with open('best_knn.pkl', 'rb') as file_1:
    best_knn = pickle.load(file_1)


def run():
    st.title('Healthcare Test Results')
    
    with st.form('Predict Default'):

        # Input data dari pengguna
        st.subheader('Personal Data')
        age = st.slider('Age', min_value=0, max_value=100)
        # Membagi layout menjadi dua kolom
        col1, col2 = st.columns(2)
        # Widget radio untuk pilihan Gender di kolom pertama
        with col1:
            gender = st.radio('Gender', ['Male', 'Female'])
        # Widget radio untuk pilihan Gender di kolom pertama
        with col2:
            blood_type = st.radio('Blood Type', ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])
    
        st.divider()
    
        st.subheader('Medical Record')
        medical_condition = st.selectbox('Medical Condition', ['Diabetes', 'Asthma', 'Obesity', 'Arthritis', 'Hypertension', 'Cancer'])
        admission_type = st.selectbox('Admission Type', ['Emergency', 'Urgent', 'Elective'])
        medication = st.selectbox('Medication', ['Aspirin', 'Lipitor', 'Penicillin', 'Paracetamol', 'Ibuprofen'])

        st.divider()
    
        st.subheader('Payment Information')
        length_of_stay = st.slider('Length of Stay (days)', min_value=0, max_value=30)
        insurance_provider = st.selectbox('Insurance Provider', ['Cigna', 'Blue Cross', 'Aetna', 'UnitedHealthCare', 'Medicare'])
        billing_amount = st.number_input('Billing Amount', min_value= 0, max_value= 50000)

        submit_button = st.form_submit_button('Predict Test Results')

    # Ketika tombol Predict ditekan
    if submit_button:
        # Siapkan data input untuk prediksi
        df_inf = {
            'age': age,
            'gender': gender,
            'blood_type': blood_type,
            'medical_condition': medical_condition,
            'admission_type': admission_type,
            'medication': medication,
            'length_of_stay': length_of_stay,
            'medication': medication,
            'insurance_provider': insurance_provider,
            'billing_amount': billing_amount,
        }

        df_inf = pd.DataFrame([df_inf])
        prediction = best_knn.predict(df_inf)

        # Display predicted test results in Streamlit
        st.title('Prediction Result')
        if prediction == 0:
            st.write('Patient is Abnormal')
        elif prediction == 1:
            st.write('Patient is Inconclusive')
        elif prediction == 2:
            st.write('Patient is Normal')


if __name__ == '__main__':
    run()
