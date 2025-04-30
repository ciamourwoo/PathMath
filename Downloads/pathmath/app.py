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
if "game_selesai" not in st.session_state:
    st.session_state["game_selesai"] = False

# ===== Data Soal Gaya Anak SD =====
soal_bank = {
    "Pecahan": {
        1: ("Ayo bantu Kak Rina menyederhanakan pecahan 6/8 supaya lebih kecil tapi nilainya tetap sama!", "3/4", "Gunakan jurus 'bagi sama'! Bagi angka atas dan bawah dengan angka yang sama ya!"),
        2: ("Monster angka mengacak-acak pecahan 20/25! Cepat sederhanakan sebelum waktunya habis!", "4/5", "Coba cari angka yang bisa membagi 20 dan 25. Gunakan jurus 'bagi bareng' yuk!"),
        3: ("Di kebun Kak Udin, 6 dari 8 bagian ditanami sayur. Tapi 4 bagian mau ditanami bunga. Berapa bagian yang masih untuk sayur? Bantu Kak Udin, yuk!", "2/8", "Ingat, kamu bisa kurangi dulu jumlah bagian, lalu sederhanakan kalau bisa ya!")
    },
    "Pola Bilangan": {
        1: ("Lihat pola ini ya: 2, 4, 6, ... Nah, angka ke-5 berapa ya?", "10", "Pola ini naik 2 terus, coba hitung satu per satu ya!"),
        2: ("Pola ini seru! 5, 10, 15, ... Nah, angka ke-6 kira-kira berapa?", "30", "Tambah terus dengan angka 5, seperti naik tangga angka!"),
        3: ("Bayangkan kamu sedang naik tangga: 1, 3, 6, 10... Berapa ya anak tangga ke-7?", "28", "Tiap langkah kamu tambahkan 1 angka lebih besar, yuk coba hitung!")
    },
    "KPK dan FPB": {
        1: ("Kak Nina mau beli pensil. Pensil 6 dan 8 datang tiap beberapa menit. Kapan datang bersamaan? Cari KPK-nya yuk!", "24", "Coba tulis kelipatan 6 dan 8, lalu cari yang sama dan paling kecil ya!"),
        2: ("Kak Riko punya 18 kelereng dan Kak Budi punya 24. Berapa kelereng terbanyak yang bisa dibagi rata ke teman-teman?", "6", "Coba cari angka yang bisa bagi 18 dan 24, yang paling besar ya!"),
        3: ("Kapan ya 9 dan 12 akan bersamaan lagi di lomba lari kelipatan? Cari KPK-nya yuk!", "36", "Coba tulis kelipatan keduanya, lalu temukan yang sama dan paling kecil.")
    },
    "Luas dan Volume": {
        1: ("Ada karpet persegi panjang, panjangnya 5 cm dan lebarnya 3 cm. Berapa luasnya ya?", "15", "Panjang kali lebar, gampang kan? Coba hitung ya!"),
        2: ("Sebuah kubus punya sisi 4 cm. Nah, berapa ya volumenya?", "64", "Pakai rumus sisi x sisi x sisi. Yuk coba hitung bareng!"),
        3: ("Sebuah segitiga punya alas 6 cm dan tinggi 4 cm. Yuk cari luasnya!", "12", "Gunakan jurus segitiga: setengah dikali alas dikali tinggi!")
    },
    "Bangun Datar": {
        1: ("Sebuah segitiga punya sisi 3 cm, 4 cm, dan 5 cm. Berapa kelilingnya?", "12", "Keliling itu jumlah semua sisi. Tambah semua ya!"),
        2: ("Sebuah persegi punya sisi 7 cm. Yuk cari kelilingnya!", "28", "Keliling persegi itu 4 dikali sisi. Gampang kan?"),
        3: ("Sebuah lingkaran punya jari-jari 7 cm. Berapa kelilingnya? (pakai π = 22/7)", "44", "Gunakan rumus: 2 × π × jari-jari. Coba masukkan angkanya!")
    }
}

# ===== Halaman IDENTITAS =====
if st.session_state["halaman"] == "identitas":
    st.title("🎮 Selamat Datang di PathMath - Petualangan Soal Matematika!")
    st.write("Ayo mulai perjalanan serumu dalam dunia angka dan bentuk!")

    with st.form("form_identitas"):
        nama = st.text_input("Siapa nama kamu?")
        materi = st.selectbox("Pilih dunia petualangan yang ingin kamu masuki:", 
            ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"])
        submit = st.form_submit_button("🎲 Mulai Petualangan!")

    if submit:
        if nama.strip() != "" and materi != "":
            st.session_state["nama"] = nama
            st.session_state["materi"] = materi
            st.session_state["halaman"] = "soal"
        else:
            st.warning("Yuk lengkapi nama dan pilih dunia petualanganmu dulu!")

# ===== Halaman SOAL =====
if st.session_state["halaman"] == "soal":
    st.title(f"🧠 Materi: {st.session_state['materi']} | Level: {st.session_state['level']}")
    st.write(f"Halo {st.session_state['nama']}! Yuk kita lanjut petualanganmu di level ini!")

    materi = st.session_state["materi"]
    level = st.session_state["level"]

    soal, jawaban_benar, penjelasan = soal_bank[materi][level]
    st.subheader(f"🎯 Soal Level {level}")
    st.write(soal)

    jawaban_user = st.text_input("Jawabanmu apa nih?", key=f"jawaban_{level}")

    if st.button("🚀 Kirim Jawaban"):
        if jawaban_user.strip() == jawaban_benar:
            st.success("🎉 Keren! Jawabanmu benar!")
            if level == 3:
                st.session_state["game_selesai"] = True
                st.session_state["halaman"] = "identitas"
            else:
                st.session_state["level"] = min(3, level + 1)
        else:
            st.error("😅 Wah, masih belum tepat nih.")
            st.info(f"🧩 Petunjuk: {penjelasan}")

        if st.session_state["game_selesai"]:
            st.success("🏆 Selamat! Kamu sudah menyelesaikan semua level petualangan!")
            if st.button("🔄 Kembali ke Halaman Awal"):
                st.session_state["halaman"] = "identitas"
                st.session_state["level"] = 1
                st.session_state["nomor_soal"] = 1
                st.session_state["game_selesai"] = False
        else:
            if st.button("➡️ Lanjut ke Level Berikutnya"):
                st.rerun()
