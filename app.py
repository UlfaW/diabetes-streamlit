import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model_diabetes.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Prediksi Penyakit Diabetes")

st.write("Input Data Pasien")

pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bloodpressure = st.number_input("BloodPressure")
skinthickness = st.number_input("SkinThickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("DiabetesPedigreeFunction")
age = st.number_input("Age")

if st.button("Prediksi"):

    data = np.array([[
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    data = scaler.transform(data)

    hasil = model.predict(data)

    if hasil[0] == 1:
        st.error("Pasien Terindikasi Diabetes")
    else:
        st.success("Pasien Tidak Diabetes")