import streamlit as st
import numpy as np
import pickle

# ======================
# CONFIG
# ======================

st.set_page_config(
    page_title="Prediksi Penyakit Diabetes",
    layout="wide"
)

# ======================
# LOAD CSS
# ======================

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# LOAD MODEL
# ======================

model = pickle.load(open("model_diabetes.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ======================
# LAYOUT
# ======================

left, right = st.columns([1,1])

# ======================
# LEFT SIDE
# ======================

with left:

    st.markdown("""
    <div class="hero-title">
        Prediksi Penyakit<br>
        <span>Diabetes</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-subtitle">
        Sistem multi-analisa kesehatan pasien
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-grid">

        <div class="info-card">
            <div class="card-icon">📈</div>
            <div class="card-title">Risiko Diabetes</div>
            <div class="card-text">
                Hasil prediksi diabetes akan tampil di sini
            </div>
        </div>

        <div class="info-card">
            <div class="card-icon">⚖️</div>
            <div class="card-title">Analisa BMI</div>
            <div class="card-text">
                Analisa BMI pasien akan tampil di sini.
            </div>
        </div>

        <div class="info-card">
            <div class="card-icon">❤️</div>
            <div class="card-title">Tekanan Darah</div>
            <div class="card-text">
                Monitoring tekanan darah pasien
            </div>
        </div>

        <div class="info-card">
            <div class="card-icon">💧</div>
            <div class="card-title">Kadar Gula</div>
            <div class="card-text">
                Monitoring kadar gula darah pasien
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

# ======================
# RIGHT SIDE
# ======================

with right:

    st.markdown("""
    <div class="form-box">

        <div class="form-title">
            👤 Input Data Pasien
        </div>

        <div class="form-subtitle">
            Isi data kesehatan pasien untuk memulai prediksi
        </div>

    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input(
        "Nama Pasien",
        placeholder="Masukkan nama pasien"
    )

    c1, c2 = st.columns(2)

    with c1:

        pregnancies = st.number_input("Pregnancies", 0.0)
        bloodpressure = st.number_input("Tekanan Darah", 0.0)
        insulin = st.number_input("Insulin", 0.0)
        dpf = st.number_input("DPF", 0.0)

    with c2:

        glucose = st.number_input("Kadar Gula Darah", 0.0)
        skin = st.number_input("Skin Thickness", 0.0)
        bmi = st.number_input("BMI", 0.0)
        age = st.number_input("Usia", 0.0)

    hasil_teks = "Hasil prediksi akan muncul di sini."

    if st.button("✨ Prediksi Diabetes"):

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
            hasil_teks = f"{nama} Terindikasi Diabetes"
        else:
            hasil_teks = f"{nama} Tidak Diabetes"

    st.markdown(f"""
    <div class="result-box">

        <div class="result-title">
            Hasil Prediksi
        </div>

        <div class="result-text">
            {hasil_teks}
        </div>

    </div>
    """, unsafe_allow_html=True)
