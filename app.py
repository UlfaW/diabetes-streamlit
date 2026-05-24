import streamlit as st

# 1. Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Prediksi Penyakit Diabetes",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Memuat File CSS Eksternal
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 3. Grid Utama Layar (Kiri: Dashboard, Kanan: Form Input Pasien)
col_left, col_right = st.columns([1.1, 1], gap="large")

# ==================== SISI KIRI (INFORMASI & DASHBOARD) ====================
with col_left:

    st.markdown("<h1 style='font-size: 3rem; font-weight: 800; margin-bottom: 0px;'>Prediksi Penyakit</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3.5rem; font-weight: 800; color: #3b82f6; margin-top: -20px; margin-bottom: 10px;'>Diabetes</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='color: #94a3b8; font-size: 1.1rem; margin-bottom: 30px;'>
            Sistem multi-analisa kesehatan pasien berbasis</span>.
        </p>
    """, unsafe_allow_html=True)
    
    card_col1, card_col2 = st.columns(2)
    with card_col1:
        st.markdown("""
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(16, 185, 129, 0.1); color: #10b981;">📈</div>
                <div class="card-title">Risiko Diabetes</div>
                <div class="card-desc">Hasil prediksi diabetes akan tampil di sini.</div>
            </div>
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(239, 68, 68, 0.1); color: #ef4444;">❤️</div>
                <div class="card-title">Tekanan Darah</div>
                <div class="card-desc">Monitoring tekanan darah pasien.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with card_col2:
        st.markdown("""
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(245, 158, 11, 0.1); color: #f59e0b;">⚖️</div>
                <div class="card-title">Analisa BMI</div>
                <div class="card-desc">Analisa BMI pasien akan tampil di sini.</div>
            </div>
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(59, 130, 246, 0.1); color: #3b82f6;">💧</div>
                <div class="card-title">Kadar Gula</div>
                <div class="card-desc">Monitoring kadar gula darah pasien.</div>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
        <div class="warning-box">
            <span style="font-size: 20px; color: #3b82f6;">ℹ️</span>
            <div>
                <strong>Sistem ini hanya untuk membantu analisis.</strong><br>
                Bukan pengganti diagnosis dokter.
            </div>
        </div>
    """, unsafe_allow_html=True)


# ==================== SISI KANAN (FORM INPUT PASIEN) ====================
with col_right:
    # REVISI FIX: Menggunakan container resmi Streamlit agar layout simetris & rapi tanpa bug garis kosong
    with st.container(border=True):
        
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background-color: rgba(59, 130, 246, 0.1); padding: 10px; border-radius: 12px; font-size: 24px;">👤</div>
                <div>
                    <h2 style="margin: 0; font-size: 1.5rem; font-weight: bold; color: white;">Input Data Pasien</h2>
                    <p style="margin: 0; color: #94a3b8; font-size: 0.9rem;">Isi data kesehatan pasien</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Input Nama Pasien (Label teks otomatis berwarna putih dari CSS)
        nama_pasien = st.text_input("Nama Pasien", placeholder="Masukkan nama pasien")
        
        # Form Input Angka terbagi menjadi 2 sub-kolom
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            pregnancies = st.number_input("Pregnancies", min_value=0, step=1, value=0)
            tekanan_darah = st.number_input("Tekanan Darah", min_value=0.0, step=1.0, value=0.0)
            insulin = st.number_input("Insulin", min_value=0.0, step=1.0, value=0.0)
            diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.000, step=0.001, format="%.3f", value=0.000)
            
        with f_col2:
            gula_darah = st.number_input("Kadar Gula Darah", min_value=0.0, step=1.0, value=0.0)
            skin_thickness = st.number_input("Skin Thickness", min_value=0.0, step=1.0, value=0.0)
            bmi = st.number_input("BMI", min_value=0.0, step=0.1, value=0.0)
            usia = st.number_input("Usia", min_value=0, step=1, value=0)
            
        # Tombol Prediksi
        btn_prediksi = st.button("Prediksi Diabetes")
        
        # Box Hasil Prediksi di bagian paling bawah form
        st.markdown("""
            <div class="result-box">
                <div style="font-weight: bold; color: #3b82f6; font-size: 1.05rem;">Hasil Prediksi</div>
                <div style="color: #94a3b8; font-size: 0.9rem; margin-top: 2px;">Hasil prediksi akan muncul di sini</div>
            </div>
        """, unsafe_allow_html=True)
