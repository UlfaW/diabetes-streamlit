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

# 3. Inisialisasi State Awal (Jika belum diklik, teks bawaan yang muncul)
if "risiko_status" not in st.session_state:
    st.session_state.risiko_status = "Hasil prediksi diabetes akan tampil di sini."
if "bmi_status" not in st.session_state:
    st.session_state.bmi_status = "Analisa BMI pasien akan tampil di sini."
if "tensi_status" not in st.session_state:
    st.session_state.tensi_status = "Monitoring tekanan darah pasien."
if "gula_status" not in st.session_state:
    st.session_state.gula_status = "Monitoring kadar gula darah pasien."
if "hasil_teks" not in st.session_state:
    st.session_state.hasil_teks = "Hasil analisa lengkap akan muncul di sini setelah tombol diklik."

# 4. Grid Utama Layar (Kiri: Dashboard, Kanan: Form Input Pasien)
col_left, col_right = st.columns([1.1, 1], gap="large")

# ==================== SISI KIRI (INFORMASI & DASHBOARD DINAMIS) ====================
with col_left:
    st.markdown("""
        <div style='display: flex; align-items: center; gap: 10px; margin-bottom: -10px;'>
            <span style='font-size: 35px;'>💙</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 style='font-size: 3rem; font-weight: 800; margin-bottom: 0px;'>Prediksi Penyakit</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 3.5rem; font-weight: 800; color: #3b82f6; margin-top: -20px; margin-bottom: 10px;'>Diabetes</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='color: #94a3b8; font-size: 1.1rem; margin-bottom: 30px;'>
            Sistem multi-analisa kesehatan pasien berbasis <span style='color: #3b82f6; font-weight: bold;'>Decision Tree</span>.
        </p>
    """, unsafe_allow_html=True)
    
    # Grid 4 Buah Kartu yang nilainya mengambil dari session_state (bisa berubah otomatis)
    card_col1, card_col2 = st.columns(2)
    with card_col1:
        st.markdown(f"""
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(16, 185, 129, 0.1); color: #10b981;">📈</div>
                <div class="card-title">Risiko Diabetes</div>
                <div class="card-desc">{st.session_state.risiko_status}</div>
            </div>
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(239, 68, 68, 0.1); color: #ef4444;">❤️</div>
                <div class="card-title">Tekanan Darah</div>
                <div class="card-desc">{st.session_state.tensi_status}</div>
            </div>
        """, unsafe_allow_html=True)
        
    with card_col2:
        st.markdown(f"""
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(245, 158, 11, 0.1); color: #f59e0b;">⚖️</div>
                <div class="card-title">Analisa BMI</div>
                <div class="card-desc">{st.session_state.bmi_status}</div>
            </div>
            <div class="dashboard-card">
                <div class="card-icon" style="background-color: rgba(59, 130, 246, 0.1); color: #3b82f6;">💧</div>
                <div class="card-title">Kadar Gula</div>
                <div class="card-desc">{st.session_state.gula_status}</div>
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
    with st.container(border=True):
        
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="background-color: rgba(59, 130, 246, 0.1); padding: 10px; border-radius: 12px; font-size: 24px;">👤</div>
                <div>
                    <h2 style="margin: 0; font-size: 1.5rem; font-weight: bold; color: white;">Input Data Pasien</h2>
                    <p style="margin: 0; color: #94a3b8; font-size: 0.9rem;">Isi data kesehatan pasien untuk memulai prediksi AI.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        nama_pasien = st.text_input("Nama Pasien", placeholder="Masukkan nama pasien")
        
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            pregnancies = st.number_input("Pregnancies", min_value=0, step=1, value=0)
            tekanan_darah = st.number_input("Tekanan Darah (mm Hg)", min_value=0.0, step=1.0, value=0.0)
            insulin = st.number_input("Insulin", min_value=0.0, step=1.0, value=0.0)
            diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.000, step=0.001, format="%.3f", value=0.000)
            
        with f_col2:
            gula_darah = st.number_input("Kadar Gula Darah (mg/dL)", min_value=0.0, step=1.0, value=0.0)
            skin_thickness = st.number_input("Skin Thickness", min_value=0.0, step=1.0, value=0.0)
            bmi = st.number_input("BMI", min_value=0.0, step=0.1, value=0.0)
            usia = st.number_input("Usia", min_value=0, step=1, value=0)
            
        btn_prediksi = st.button("✨ Prediksi Diabetes")
        
        # LOGIKA PROSES ANALISA SAAT TOMBOL DIKLIK
        if btn_prediksi:
            if nama_pasien.strip() == "":
                st.warning("Silakan masukkan nama pasien terlebih dahulu!")
            else:
                # 1. LOGIKA SIMULASI DIAGNOSIS UTAMA DIABETES
                # (Bisa diganti dengan hasil model: model.predict([[...]]))
                if gula_darah > 140.0 or bmi > 25.0:
                    st.session_state.risiko_status = "🚨 Risiko Tinggi (Positif)"
                    status_akhir = "Risiko Tinggi"
                else:
                    st.session_state.risiko_status = "🟢 Risiko Rendah (Negatif)"
                    status_akhir = "Risiko Rendah"
                
                # 2. LOGIKA ANALISA BMI DINAMIS
                if bmi == 0:
                    st.session_state.bmi_status = "Data BMI kosong."
                elif bmi < 18.5:
                    st.session_state.bmi_status = f"BMI {bmi:.1f}: Berat Badan Kurang (Underweight)."
                elif 18.5 <= bmi < 25.0:
                    st.session_state.bmi_status = f"BMI {bmi:.1f}: Normal / Ideal."
                else:
                    st.session_state.bmi_status = f"BMI {bmi:.1f}: Obesitas / Kelebihan Berat Badan."
                    
                # 3. LOGIKA ANALISA TEKANAN DARAH DINAMIS
                if tekanan_darah == 0:
                    st.session_state.tensi_status = "Data tekanan darah kosong."
                elif tekanan_darah < 80:
                    st.session_state.tensi_status = f"Tensi {tekanan_darah:.0f} mmHg: Tekanan Darah Rendah (Hipotensi)."
                elif 80 <= tekanan_darah <= 120:
                    st.session_state.tensi_status = f"Tensi {tekanan_darah:.0f} mmHg: Normal."
                else:
                    st.session_state.tensi_status = f"Tensi {tekanan_darah:.0f} mmHg: Tekanan Darah Tinggi (Hipertensi)."
                    
                # 4. LOGIKA ANALISA KADAR GULA DARAH DINAMIS
                if gula_darah == 0:
                    st.session_state.gula_status = "Data kadar gula kosong."
                elif gula_darah < 100:
                    st.session_state.gula_status = f"Gula {gula_darah:.0f} mg/dL: Normal (Puasa)."
                elif 100 <= gula_darah <= 140:
                    st.session_state.gula_status = f"Gula {gula_darah:.0f} mg/dL: Prediabetes."
                else:
                    st.session_state.gula_status = f"Gula {gula_darah:.0f} mg/dL: Sangat Tinggi (Diabetes)."
                
                # 5. KOTAK INFORMASI RINGKASAN DI BAWAH
                st.session_state.hasil_teks = f"Analisis AI selesai untuk pasien <b>{nama_pasien}</b>. Status kesehatan menunjukkan indikasi <b>{status_akhir}</b> terhadap diabetes berdasarkan parameter input."
                
                # Memuat ulang halaman agar data langsung muncul seketika di semua kartu
                st.rerun()
        
        # Box Hasil Prediksi di bawah form
        st.markdown(f"""
            <div class="result-box">
                <div style="font-weight: bold; color: #3b82f6; font-size: 1.05rem;">Hasil Prediksi Analisis</div>
                <div style="color: #ffffff; font-size: 0.9rem; margin-top: 5px; line-height: 1.4;">{st.session_state.hasil_teks}</div>
            </div>
        """, unsafe_allow_html=True)
