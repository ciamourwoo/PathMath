import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Isi halaman aplikasi
st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

# Form input identitas siswa
with st.form("form_identitas"):
    nama = st.text_input("Nama Lengkap")
    kelas = st.selectbox("Kelas", ["4", "5", "6"])
    materi = st.selectbox("Materi yang akan dikerjakan", ["Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"])
    
    submit_button = st.form_submit_button("Mulai Mengerjakan")

# Jika tombol diklik
if submit_button:
    st.success(f"Halo {nama} dari kelas {kelas}, selamat mengerjakan materi {materi}!")
    # Simpan data identitas siswa ke session (opsional)
    st.session_state["nama"] = nama
    st.session_state["kelas"] = kelas
    st.session_state["materi"] = materi

