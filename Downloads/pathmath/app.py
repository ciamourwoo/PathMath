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
        1: ("Sederhanakan: 6/8", "3/4", "Hmm, kita bisa bikin angka ini lebih kecil! Coba bagi 6 dan 8 dengan angka yang sama, misalnya 2."),
        2: ("Sederhanakan: 10/15", "2/3", "Coba bagi 10 dan 15 dengan angka 5, pasti ketemu jawabannya!"),
        3: ("Sederhanakan: 14/21", "2/3", "Ada angka yang bisa kita bagi, coba bagi 14 dan 21 dengan angka 7!"),
    },
    "Pola Bilangan": {
        1: ("Angka ke-5 dari pola: 2, 4, 6, ...", "10", "Pola ini bertambah 2 setiap langkah. Coba tambahkan angka 2, 4, 6, 8, dan 10!"),
        2: ("Angka ke-6 dari pola: 5, 10, 15, ...", "30", "Setiap angka bertambah 5, jadi angka ke-6 adalah 30!"),
        3: ("Angka ke-7 dari pola: 1, 3, 6, 10, ...", "28", "Pola bertambah dengan angka yang terus berubah. Coba hitung lagi angka ke-7!"),
    },
    "KPK dan FPB": {
        1: ("Tentukan KPK dari 6 dan 8", "24", "Coba cari angka yang pertama kali muncul sebagai kelipatan dari 6 dan 8!"),
        2: ("Tentukan FPB dari 18 dan 24", "6", "Cari angka yang bisa membagi 18 dan 24 tanpa ada sisa. Apa itu?"),
        3: ("Tentukan KPK dari 9 dan 12", "36", "Coba temukan kelipatan terkecil dari 9 dan 12. Bisa kamu temukan 36?"),
    },
    "Luas dan Volume": {
        1: ("Luas persegi panjang dengan panjang 5 cm dan lebar 3 cm?", "15", "Luas = panjang × lebar. Jadi 5 cm × 3 cm, gampang kan?"),
        2: ("Volume kubus dengan sisi 4 cm?", "64", "Volume = sisi × sisi × sisi. Jadi 4 cm × 4 cm × 4 cm = 64!"),
        3: ("Luas segitiga dengan alas 6 cm dan tinggi 4 cm?", "12", "Luas segitiga = 1/2 × alas × tinggi. Coba hitung 1/2 × 6 cm × 4 cm!"),
    },
    "Bangun Datar": {
        1: ("Keliling segitiga dengan sisi 3 cm, 4 cm, dan 5 cm?", "12", "Keliling = jumlah sisi segitiga. 3 cm + 4 cm + 5 cm = 12 cm!"),
        2: ("Keliling persegi dengan sisi 7 cm?", "28", "Keliling = 4 × sisi. Jadi 4 × 7 cm = 28 cm!"),
        3: ("Keliling lingkaran dengan jari-jari 7 cm (pakai pi=22/7)?", "44", "Keliling = 2 × π × r. Pakai pi 22/7, hitung deh!"),
    }
}

# ===== Halaman IDENTITAS =====
if st.session_state["halaman"] == "identitas":
    st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
    st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang seru!")

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
    
    # Menambahkan cerita di setiap level
    if st.session_state["level"] == 1:
        st.write("Pahlawan kita baru memulai perjalanan, dan mereka harus menyelesaikan tantangan pertama untuk melanjutkan...")
    elif st.session_state["level"] == 2:
        st.write("Sang pahlawan hampir sampai di tujuan, tapi rintangan semakin berat. Haruskah mereka terus maju?")
    elif st.session_state["level"] == 3:
        st.write("Ini adalah tantangan terakhir! Pahlawan kita hampir menjadi legenda, hanya satu rintangan lagi yang harus diatasi.")
    
    st.write(f"Halo {st.session_state['nama']}, selamat mengerjakan!")

    materi = st.session_state["materi"]
    level = st.session_state["level"]

    soal, jawaban_benar, penjelasan = soal_bank[materi][level]
    st.subheader(f"Soal Level {level}")
    st.write(soal)

    jawaban_user = st.text_input("Jawaban kamu:", key=f"jawaban_{level}")

    if st.button("Kirim Jawaban"):
        if jawaban_user.strip() == jawaban_benar:
            st.success("Jawaban benar! Pahlawan kita berhasil melewati rintangan!")
            if level == 3:
                st.session_state["game_selesai"] = True
                st.session_state["halaman"] = "identitas"  # Mengarahkan ke halaman identitas setelah selesai
        else:
            st.error("Jawaban salah. Pahlawan kita tersandung batu, tetapi masih ada harapan!")
            # Penjelasan yang lebih menyenangkan
            st.info(f"Petunjuk: {penjelasan}. Ingat, matematika itu seperti permainan yang seru, yuk coba lagi!")

