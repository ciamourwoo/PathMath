import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Inisialisasi state
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "identitas"
if "nama" not in st.session_state:
    st.session_state["nama"] = ""
if "materi" not in st.session_state:
    st.session_state["materi"] = ""

# Halaman IDENTITAS
if st.session_state["halaman"] == "identitas":
    st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
    st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

    with st.form("form_identitas"):
        nama = st.text_input("Nama Lengkap", value=st.session_state["nama"])
        materi = st.selectbox(
            "Materi yang akan dikerjakan",
            ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"],
            index=0
        )
        submit = st.form_submit_button("Mulai Mengerjakan")

        if submit:
            if nama != "" and materi != "":
                st.session_state["nama"] = nama
                st.session_state["materi"] = materi
                st.session_state["halaman"] = "soal"
                st.experimental_rerun()
            else:
                st.warning("Harap isi nama dan pilih materi terlebih dahulu!")

# Halaman SOAL
elif st.session_state["halaman"] == "soal":
    st.title(f"Materi: {st.session_state['materi']}")
    st.write(f"Halo {st.session_state['nama']}, selamat mengerjakan!")

    materi = st.session_state["materi"]

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
    elif materi == "Luas dan Volume":
        st.subheader("1. Luas dan Volume")
        st.write("Luas persegi panjang dengan panjang 5 cm dan lebar 3 cm?")
        st.text_input("Jawaban:")
    elif materi == "Bangun Datar":
        st.subheader("1. Bangun Datar")
        st.write("Keliling segitiga dengan sisi 3 cm, 4 cm, dan 5 cm?")
        st.text_input("Jawaban:")
