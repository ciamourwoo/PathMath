import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Inisialisasi halaman saat pertama kali
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "identitas"

# Fungsi pindah ke halaman soal
def mulai_soal():
    # Validasi inputan (jika ada yang kosong)
    if st.session_state.nama and st.session_state.materi:
        st.session_state["halaman"] = "soal"
    else:
        st.warning("Harap lengkapi semua data sebelum melanjutkan!")

# Halaman identitas (halaman pertama)
if st.session_state["halaman"] == "identitas":
    st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
    st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

    with st.form("form_identitas"):
        # Form input identitas siswa
        st.session_state.nama = st.text_input("Nama Lengkap", key="nama")
        st.session_state.materi = st.selectbox("Materi yang akan dikerjakan", ["", "Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"], key="materi")

        submit_button = st.form_submit_button("Mulai Mengerjakan", on_click=mulai_soal):
        pass


# Halaman soal sesuai materi (halaman kedua)
elif st.session_state["halaman"] == "soal":
    st.title(f"Materi: {st.session_state.materi}")
    st.write(f"Halo {st.session_state.nama}, selamat mengerjakan!")
     else:
            st.warning("Harap lengkapi semua data sebelum melanjutkan!")

    # Tentukan soal untuk setiap materi
    soal_materi = {
        "Pecahan": [
            {"soal": "Sederhanakan: 6/8", "jawaban": "3/4"},
            {"soal": "Sederhanakan: 12/16", "jawaban": "3/4"}
        ],
        "Pola Bilangan": [
            {"soal": "Angka ke-5 dari pola: 2, 4, 6, ...", "jawaban": "10"},
            {"soal": "Angka ke-7 dari pola: 1, 4, 7, ...", "jawaban": "22"}
        ],
        "KPK dan FPB": [
            {"soal": "Tentukan KPK dari 6 dan 8", "jawaban": "24"},
            {"soal": "Tentukan FPB dari 12 dan 18", "jawaban": "6"}
        ],
        "Luas dan Volume": [
            {"soal": "Luas persegi panjang dengan panjang 5 cm dan lebar 3 cm?", "jawaban": "15 cm²"},
            {"soal": "Volume balok dengan panjang 4 cm, lebar 3 cm, dan tinggi 6 cm?", "jawaban": "72 cm³"}
        ],
        "Bangun Datar": [
            {"soal": "Keliling segitiga dengan sisi 3 cm, 4 cm, dan 5 cm?", "jawaban": "12 cm"},
            {"soal": "Luas lingkaran dengan jari-jari 7 cm?", "jawaban": "154 cm²"}
        ]
    }

    # Pilih soal berdasarkan materi yang dipilih
    materi = st.session_state.materi
    soal_list = soal_materi.get(materi, [])

    # Menampilkan soal jika ada
    if soal_list:
        if 'nomor_soal' not in st.session_state:
            st.session_state.nomor_soal = 1

        current = st.session_state.nomor_soal - 1
        st.subheader(f"Soal {st.session_state.nomor_soal}")
        st.write(soal_list[current]["soal"])
        pilihan = st.text_input("Jawaban:", key=current)

        if st.button("Submit Jawaban"):
            benar = pilihan == soal_list[current]["jawaban"]
            if benar:
                st.success("Jawaban benar! 🎉")
            else:
                st.error("Jawaban salah 😬")

            if st.session_state.nomor_soal < len(soal_list):
                st.session_state.nomor_soal += 1
                st.experimental_rerun()
            else:
                st.balloons()
                st.markdown("### Selesai! Terima kasih sudah mengerjakan 😄")
