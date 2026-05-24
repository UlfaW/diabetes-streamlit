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

model = pickle.load(open("model_diabetes.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# =========================
# LAYOUT
# =========================

left, right = st.columns([1.05, 1])

# =========================
# LEFT SIDE
# =========================

with left:

    st.markdown("""
    <div class="main-title">
        Prediksi Penyakit<br>
        <span>Diabetes</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
        Sistem multi-analisa kesehatan pasien<br>
        berbasis <span>Decision Tree.</span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
            <div class="icon green">📈</div>

            <div class="card-title">
                Risiko Diabetes
            </div>

            <div class="card-text">
                Hasil prediksi diabetes<br>
                akan tampil di sini.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
            <div class="icon yellow">⚖️</div>

            <div class="card-title">
                Analisa BMI
            </div>

            <div class="card-text">
                Analisa BMI pasien<br>
                akan tampil di sini.
            </div>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:

        st.markdown("""
        <div class="card">
            <div class="icon red">❤️</div>

            <div class="card-title">
                Tekanan Darah
            </div>

            <div class="card-text">
                Monitoring tekanan darah pasien.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown("""
        <div class="card">
            <div class="icon blue">💧</div>

            <div class="card-title">
                Kadar Gula
            </div>

            <div class="card-text">
                Monitoring kadar gula darah pasien.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-box">
        ℹ️ Sistem ini hanya untuk membantu analisis,
        bukan pengganti diagnosis dokter.
    </div>
    """, unsafe_allow_html=True)

# =========================
# RIGHT SIDE
# =========================

with right:

    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    st.markdown("""
    <div class="form-header">

        <div class="form-icon">
            👤
        </div>

        <div>

            <div class="form-title">
                Input Data Pasien
            </div>

            <div class="form-subtitle">
                Isi data kesehatan pasien untuk memulai prediksi.
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    nama = st.text_input(
        "Nama Pasien",
        placeholder="Masukkan nama pasien"
    )

    c1, c2 = st.columns(2)

    with c1:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0.0
        )

        bloodpressure = st.number_input(
            "Tekanan Darah",
            min_value=0.0
        )

        insulin = st.number_input(
            "Insulin",
            min_value=0.0
        )

        dpf = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0
        )

    with c2:

        glucose = st.number_input(
            "Kadar Gula Darah",
            min_value=0.0
        )

        skin = st.number_input(
            "Skin Thickness",
            min_value=0.0
        )

        bmi = st.number_input(
            "BMI",
            min_value=0.0
        )

        age = st.number_input(
            "Usia",
            min_value=0.0
        )

    hasil_prediksi = "Hasil prediksi akan muncul di sini."

    if st.button("Prediksi Diabetes"):

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
            hasil_prediksi = f"{nama} Terindikasi Diabetes"
        else:
            hasil_prediksi = f"{nama} Tidak Diabetes"

    st.markdown(f"""
    <div class="result-box">

        <div class="result-icon">
            ⭕
        </div>

        <div>

            <div class="result-title">
                Hasil Prediksi
            </div>

            <div class="result-text">
                {hasil_prediksi}
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
