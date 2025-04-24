import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Inisialisasi session_state
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "identitas"

# Halaman Identitas
if st.session_state["halaman"] == "identitas":
    st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
    st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

    with st.form("form_identitas"):
        st.text_input("Nama Lengkap", key="nama")
        st.selectbox(
            "Materi yang akan dikerjakan",
            ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"],
            key="materi"
        )
        submit_button = st.form_submit_button("Mulai Mengerjakan")

    if submit_button:
        if st.session_state["nama"] and st.session_state["materi"]:
            st.session_state["halaman"] = "soal"
            st.experimental_rerun()  # 🔥 ini penting untuk berpindah halaman
        else:
            st.warning("Harap lengkapi semua data sebelum melanjutkan!")

# Halaman Soal
elif st.session_state["halaman"] == "soal":
    st.title(f"Materi: {st.session_state['materi']}")
    st.write(f"Halo {st.session_state['nama']}, selamat mengerjakan!")

    materi = st.session_state["materi"]

    if materi == "Pecahan":
        st.subheader("1. Pecahan")
        st.write("Sederhanakan: 6/8")
        st.text_input("Jawaban:", key="jawaban_pecahan")

    elif materi == "Pola Bilangan":
        st.subheader("1. Pola Bilangan")
        st.write("Angka ke-5 dari pola: 2, 4, 6, ...")
        st.text_input("Jawaban:", key="jawaban_pola")

    elif materi == "KPK dan FPB":
        st.subheader("1. KPK dan FPB")
        st.write("Tentukan KPK dari 6 dan 8")
        st.text_input("Jawaban:", key="jawaban_kpk")

    elif materi == "Luas dan Volume":
        st.subheader("1. Luas dan Volume")
        st.write("Luas persegi panjang dengan panjang 5 cm dan lebar 3 cm?")
        st.text_input("Jawaban:", key="jawaban_luas")

    elif materi == "Bangun Datar":
        st.subheader("1. Bangun Datar")
        st.write("Keliling segitiga dengan sisi 3 cm, 4 cm, dan 5 cm?")
        st.text_input("Jawaban:", key="jawaban_bangun")
