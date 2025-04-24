import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Inisialisasi halaman saat pertama kali
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "identitas"

# Fungsi pindah ke halaman soal
def mulai_soal():
    if st.session_state.nama and st.session_state.materi:
        st.session_state["halaman"] = "soal"

# Halaman identitas (halaman pertama)
if st.session_state["halaman"] == "identitas":
    st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
    st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

    st.text_input("Nama Lengkap", key="nama")
    st.selectbox("Materi yang akan dikerjakan", ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"], key="materi")

    if st.button("Mulai Mengerjakan", on_click=mulai_soal):
        pass

# Halaman soal sesuai materi (halaman kedua)
elif st.session_state["halaman"] == "soal":
    st.title(f"Materi: {st.session_state.materi}")
    st.write(f"Halo {st.session_state.nama}, selamat mengerjakan!")

    # Tampilkan soal sesuai materi
    materi = st.session_state.materi

    if materi == "Pecahan":
        st.subheader("1. Pecahan")
        st.write("Sederhanakan: 6/8")
        st.text_input("Jawaban:")
    elif materi == "Pola Bilangan":
        st.subheader("1. Pola Bilangan")
        st.write("Angka ke-5 dari pola: 2, 4, 6, ...")
        st.text_input("Jawaban:")
    elif materi == "KPK dan FPB":
        st.subheader("1. KPK dan FPB")
        st.write("Tentukan KPK dari 6 dan 8")
        st.text_input("Jawaban:")
    # ... dst sesuai materi lainnya
