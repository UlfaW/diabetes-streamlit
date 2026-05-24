import streamlit as st
import numpy as np
import pickle

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Prediksi Penyakit Diabetes",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# =========================
# LOAD CSS
# =========================

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================

model = pickle.load(open('model_diabetes.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# =========================
# LAYOUT
# =========================

left, right = st.columns([1.2, 1])

# =========================
# LEFT SIDE
# =========================

with left:

    st.markdown("""
    <div class='title'>
        💙 Prediksi Penyakit Diabetes 
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='subtitle'>
        Sistem multi-analisa kesehatan pasien berbasis Desicion Tree.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class='card'>
            <h1>📈</h1>
            <h2>Risiko Diabetes</h2>
            <p>Hasil prediksi diabetes akan tampil di sini.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class='card'>
            <h1>⚖️</h1>
            <h2>Analisa BMI</h2>
            <p>Analisa BMI pasien akan tampil di sini.</p>
        </div>
        """, unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:

        st.markdown("""
        <div class='card'>
            <h1>❤️</h1>
            <h2>Tekanan Darah</h2>
            <p>Monitoring tekanan darah pasien.</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:

        st.markdown("""
        <div class='card'>
            <h1>💧</h1>
            <h2>Kadar Gula</h2>
            <p>Monitoring kadar gula darah pasien.</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# RIGHT SIDE
# =========================

with right:

    st.markdown("<div class='input-box'>", unsafe_allow_html=True)

    st.title("Input Data Pasien")

    nama = st.text_input("Nama Pasien")

    pregnancies = st.number_input("Pregnancies")
    glucose = st.number_input("Kadar Gula Darah")
    bloodpressure = st.number_input("Tekanan Darah")
    skin = st.number_input("Skin Thickness")
    insulin = st.number_input("Insulin")
    bmi = st.number_input("BMI")
    dpf = st.number_input("Diabetes Pedigree Function")
    age = st.number_input("Usia")

    if st.button("Prediksi Penyakit Diabetes"):

        data = np.array([[
            pregnancies,
            glucose,
            bloodpressure,
            skin,
            insulin,
            bmi,
            dpf,
            age
        ]])

        data = scaler.transform(data)

        hasil = model.predict(data)

        if hasil[0] == 1:

            st.error(f"{nama} Terindikasi Diabetes")

        else:

            st.success(f"{nama} Tidak Diabetes")

    st.markdown("</div>", unsafe_allow_html=True)
