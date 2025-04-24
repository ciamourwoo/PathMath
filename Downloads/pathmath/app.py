import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Isi halaman aplikasi
st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")
    
# Form input identitas siswa
with st.form("form_identitas"):
    nama = st.text_input("Nama Lengkap")
    materi = st.selectbox("Materi yang akan dikerjakan", ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"])
    
    submit_button = st.form_submit_button("Mulai Mengerjakan")

# Validasi setelah tombol diklik
if submit_button:
    if nama.strip() == "" or materi == "":
        st.error("❌ Silakan isi nama lengkap dan pilih materi terlebih dahulu!")
    else:
        st.success(f"Halo {nama}, selamat mengerjakan materi {materi}!")
        st.session_state["nama"] = nama
        st.session_state["materi"] = materi
