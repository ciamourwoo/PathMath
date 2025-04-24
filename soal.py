import streamlit as st

# Cek apakah data sudah ada
if "nama" not in st.session_state or "materi" not in st.session_state:
    st.warning("Silakan isi data terlebih dahulu di halaman utama.")
    st.stop()

# Ambil data dari session
nama = st.session_state["nama"]
materi = st.session_state["materi"]

st.title(f"Soal Matematika - Materi: {materi}")
st.write(f"Selamat mengerjakan, {nama}!")

# Soal berdasarkan materi
if materi == "Pecahan":
    st.subheader("1. Pecahan")
    st.write("Sederhanakan: 6/8")
    jawaban = st.text_input("Jawaban Anda:")
elif materi == "Pola Bilangan":
    st.subheader("1. Pola Bilangan")
    st.write("Tentukan angka ke-5 dari pola: 2, 4, 6, ...")
    jawaban = st.text_input("Jawaban Anda:")
elif materi == "KPK dan FPB":
    st.subheader("1. KPK dan FPB")
    st.write("Tentukan KPK dari 6 dan 8")
    jawaban = st.text_input("Jawaban Anda:")
elif materi == "Luas dan Volume":
    st.subheader("1. Luas dan Volume")
    st.write("Hitung luas persegi panjang 5x4 cm")
    jawaban = st.text_input("Jawaban Anda:")
elif materi == "Bangun Datar":
    st.subheader("1. Bangun Datar")
    st.write("Sebutkan nama bangun datar yang memiliki 3 sisi")
    jawaban = st.text_input("Jawaban Anda:")

# Tombol untuk submit jawaban
if st.button("Kirim Jawaban"):
    st.success(f"Jawaban '{jawaban}' berhasil dikirim!")
