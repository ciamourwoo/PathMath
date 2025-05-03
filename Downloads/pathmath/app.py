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
if "nama" not in st.session_state:
    st.session_state["nama"] = ""

# ===== Data Soal Gaya Anak SD =====
soal_bank = {
    "Pecahan": {
        1: ("Ayo sederhanakan pecahan 6/8!", "3/4", "Gunakan jurus 'bagi sama'! 6 dan 8 bisa dibagi dengan angka yang sama, misalnya 2. Yuk dicoba!"),
        2: ("Yuk, hitung: 1/2 + 1/4!", "3/4", "Eits, penyebutnya beda. Kita harus samakan dulu!. Ubah 1/2 jadi 2/4 biar sama dengan penyebut 4. Sekarang 2/4 + 1/4 = ?"),
        3: ("Rina punya 3/4 liter sirup, Andi punya 2/3 liter. Siapa lebih banyak? Rina atau Andi?", "rina", "Hmm... penyebutnya beda, yuk samakan dulu! Ubah ke penyebut 12. 3/4 = 9/12, 2/3 = 8/12 → Siapa yang lebih banyak?")
    },
    "Pola Bilangan": {
        1: ("2, 4, 6, ... Angka ke-5 berapa ya?", "10", "Pola ini naik 2 terus. Coba hitung ya: 2, 4, 6, 8, ... Tambah 2 terus sampai angka ke-5!"),
        2: ("Coba lihat pola ini ya! 5, 10, 15, ... Nah, angka ke-6 kira-kira berapa?", "30", "Tambah terus dengan angka 5. Hitung bareng yuk: 5, 10, 15, 20, 25... terus sampai angka ke-6!"),
        3: ("Bayangkan kamu sedang naik tangga: 1, 3, 6, 10... Berapa ya anak tangga ke-7?", "28", "Tiap langkah kamu tambahkan angka yang lebih besar dari sebelumnya: 1+2, lalu +3, +4... Lanjutkan sampai ke langkah ke-7 ya!")
    },
    "KPK dan FPB": {
        1: ("Berapa ya KPK dari 6 dan 8?", "24", "Coba tulis kelipatan 6: 6, 12, 18, ... dan kelipatan 8: 8, 16, 24, ... lalu cari yang sama dan paling kecil ya!"),
        2: ("Kak Riko punya 18 kelereng dan Kak Budi punya 24. Berapa kelereng terbanyak yang bisa dibagi rata ke teman-teman?", "6", "Cari angka yang bisa membagi 18 dan 24, misalnya: 6, 3... Nah, yang paling besar itu jawabannya!"),
        3: ("Ali berlari mengelilingi lapangan. Ia berlari setiap 15 menit, sementara Budi setiap 20 menit. Setelah berapa menit mereka akan berlari bersama di titik awal?", "60", "Cari KPK dari 15 dan 20. Cari angka yang sama dan paling kecil ya!")
    },
    "Luas dan Volume": {
        1: ("Ada persegi panjang yang panjangnya 5 cm dan lebarnya 3 cm. Luasnya ... cm2", "15", "Gunakan rumus: panjang × lebar. Yuk masukkan angkanya dan hitung bareng!"),
        2: ("Sebuah kubus punya sisi 4 cm. Nah, berapa ya volumenya? Volumenya ... cm3", "64", "Pakai rumus sisi × sisi × sisi. Coba hitung: sisi pertama × sisi kedua × sisi ketiga ya!"),
        3: ("Sebuah segitiga punya alas 6 cm dan tinggi 4 cm. Luasnya ... cm2", "12", "Gunakan jurus segitiga: 1/2 × alas × tinggi. Masukkan angka-angkanya yuk!")
    },
    "Bangun Datar": {
        1: ("Keliling dari segitiga yang sisinya 3 cm, 4 cm, dan 5 cm adalah ... cm", "12", "Keliling itu jumlah semua sisi. Tambahkan satu per satu ya: sisi 1 + sisi 2 + sisi 3!"),
        2: ("Sebuah persegi punya sisi 7 cm. Yuk cari kelilingnya! Kelilingnya adalah ... cm", "28", "Keliling persegi itu 4 × sisi. Masukkan angkanya yuk!"),
        3: ("Sebuah lingkaran punya jari-jari 7 cm. Kelilingnya adalah ... cm. (pakai π = 22/7)", "44", "Gunakan rumus: 2 × π × jari-jari. Jadi 2 × 22/7 × 7, yuk hitung bareng!")
    }
}

# ===== Halaman IDENTITAS =====
if st.session_state["halaman"] == "identitas" and not st.session_state["nama"]:
    st.image("C:\Users\user\Downloads/PATHMATH.png", use_container_width=True) 
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
            st.session_state["level"] = 1
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

    # Progress bar
    st.progress((level - 1) / 3)

    jawaban_user = st.text_input("Jawabanmu apa nih?", key=f"jawaban_{materi}_{level}")

    if st.button("🚀 Kirim Jawaban"):
        if jawaban_user.strip().lower() == jawaban_benar.strip().lower():
            st.success("🎉 Keren! Jawabanmu benar!")
            st.image("https://i.ibb.co/tKPYZfY/benar-bintang.gif", width=150)
            if level == 3:
                st.session_state["game_selesai"] = True
                st.session_state["halaman"] = "selesai"
            else:
                st.session_state["level"] = min(3, level + 1)
                st.rerun()
        else:
            st.error("😅 Wah, masih belum tepat nih.")
            st.image("https://i.ibb.co/ZX0zVdx/coba-lagi.gif", width=150)
            st.info(f"🧩 Petunjuk: {penjelasan}")

# ===== Halaman SELESAI =====
if st.session_state["halaman"] == "selesai" and st.session_state["game_selesai"]:
    st.balloons()
    st.success("🏆 Selamat! Kamu sudah menyelesaikan semua level petualangan!")
    st.image("https://i.ibb.co/vxN0Z1M/selamat-anak.png", width=200)

    if st.button("🔄 Kembali ke Halaman Awal"):
        st.session_state["halaman"] = "identitas"
        st.session_state["level"] = 1
        st.session_state["nomor_soal"] = 1
        st.session_state["game_selesai"] = False
        st.session_state["nama"] = ""
        st.rerun()
