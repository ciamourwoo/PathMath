import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Inisialisasi state
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "identitas"
if "level" not in st.session_state:
    st.session_state["level"] = 1
if "nomor_soal" not in st.session_state:
    st.session_state["nomor_soal"] = 1
if "skor" not in st.session_state:
    st.session_state["skor"] = 0

# ===== Data Soal Berdasarkan Level =====
soal_bank = {
    "Pecahan": {
        1: ("Sederhanakan: 6/8", "3/4"),
        2: ("Sederhanakan: 10/15", "2/3"),
        3: ("Sederhanakan: 14/21", "2/3")
    },
    "Pola Bilangan": {
        1: ("Angka ke-5 dari pola: 2, 4, 6, ...", "10"),
        2: ("Angka ke-6 dari pola: 5, 10, 15, ...", "30"),
        3: ("Angka ke-7 dari pola: 1, 3, 6, 10, ...", "28")
    },
    "KPK dan FPB": {
        1: ("Tentukan KPK dari 6 dan 8", "24"),
        2: ("Tentukan FPB dari 18 dan 24", "6"),
        3: ("Tentukan KPK dari 9 dan 12", "36")
    },
    "Luas dan Volume": {
        1: ("Luas persegi panjang dengan panjang 5 cm dan lebar 3 cm?", "15"),
        2: ("Volume kubus dengan sisi 4 cm?", "64"),
        3: ("Luas segitiga dengan alas 6 cm dan tinggi 4 cm?", "12")
    },
    "Bangun Datar": {
        1: ("Keliling segitiga dengan sisi 3 cm, 4 cm, dan 5 cm?", "12"),
        2: ("Keliling persegi dengan sisi 7 cm?", "28"),
        3: ("Keliling lingkaran dengan jari-jari 7 cm (pakai pi=22/7)?", "44")
    }
}

# ===== Halaman IDENTITAS =====
if st.session_state["halaman"] == "identitas":
    st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
    st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

    with st.form("form_identitas"):
        nama = st.text_input("Nama Lengkap")
        materi = st.selectbox("Materi yang akan dikerjakan", 
            ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"])
        submit = st.form_submit_button("Mulai Mengerjakan")

    if submit:
        if nama.strip() != "" and materi != "":
            st.session_state["nama"] = nama
            st.session_state["materi"] = materi
            st.session_state["halaman"] = "soal"
        else:
            st.warning("Harap lengkapi semua data terlebih dahulu!")

# ===== Halaman SOAL =====
if st.session_state["halaman"] == "soal":
    st.title(f"Materi: {st.session_state['materi']} | Level: {st.session_state['level']}")
    st.write(f"Halo {st.session_state['nama']}, selamat mengerjakan!")

    materi = st.session_state["materi"]
    level = st.session_state["level"]

    soal, jawaban_benar = soal_bank[materi][level]
    st.subheader(f"Soal Level {level}")
    st.write(soal)

    jawaban_user = st.text_input("Jawaban kamu:", key=f"jawaban_{level}")

    if st.button("Kirim Jawaban"):
        if jawaban_user.strip() == jawaban_benar:
            st.success("Jawaban benar! Kamu naik ke level berikutnya.")
            st.session_state["level"] = min(3, level + 1)
        else:
            st.error("Jawaban salah. Kamu tetap di level ini.")

        if level == 3:
            st.balloons()
            st.success("Selamat, kamu sudah menyelesaikan semua level!")
            if st.button("Ulangi dari awal"):
                st.session_state["halaman"] = "identitas"
                st.session_state["level"] = 1
                st.session_state["nomor_soal"] = 1
        else:
            if st.button("Lanjut ke soal berikutnya"):
                st.rerun()
