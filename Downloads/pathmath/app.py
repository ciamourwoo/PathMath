import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="PathMath", layout="centered")

# Isi halaman aplikasi
st.title("Selamat Datang di PathMath - Sistem Rekomendasi Soal Matematika")
st.write("Ayo mulai perjalananmu dalam memahami matematika dengan soal yang tepat!")

# Form input identitas siswa
with st.form("form_identitas"):
    nama = st.text_input("Nama Lengkap")
    kelas = st.selectbox("Kelas", ["4", "5", "6"])
    materi = st.selectbox("Materi yang akan dikerjakan", ["Pecahan", "Pola Bilangan", "KPK dan FPB", "Luas dan Volume", "Bangun Datar"])
    
    submit_button = st.form_submit_button("Mulai Mengerjakan")

# Jika tombol diklik
if submit_button:
    st.success(f"Halo {nama} dari kelas {kelas}, selamat mengerjakan materi {materi}!")
    # Simpan data identitas siswa ke session (opsional)
    st.session_state["nama"] = nama
    st.session_state["kelas"] = kelas
    st.session_state["materi"] = materi

import streamlit as st

# Pastikan session_state.kelas sudah ada, jika belum inisialisasi dengan None atau nilai default
if 'kelas' not in st.session_state:
    st.session_state.kelas = None  # Inisialisasi dengan nilai default (misalnya None)

# Tentukan soal untuk setiap kelas
soal_kelas = {
    "4": [
        {"soal": "Berapakah 6 + 3?", "opsi": ["7", "8", "9", "10"], "jawaban": "9"},
        {"soal": "Berapakah 5 - 2?", "opsi": ["1", "2", "3", "4"], "jawaban": "3"}
    ],
    "5": [
        {"soal": "Berapakah 12 ÷ 3?", "opsi": ["2", "3", "4", "6"], "jawaban": "4"},
        {"soal": "Berapakah 7 × 6?", "opsi": ["42", "49", "56", "63"], "jawaban": "42"}
    ],
    "6": [
        {"soal": "Berapakah 5/8 + 3/8?", "opsi": ["3/8", "4/8", "8/8", "1"], "jawaban": "1"},
        {"soal": "Berapakah 15 ÷ 5 × 3?", "opsi": ["6", "9", "12", "15"], "jawaban": "9"}
    ]
}

# Pastikan st.session_state.kelas ada sebelum mencari soal
if st.session_state.kelas:
    soal_list = soal_kelas.get(st.session_state.kelas, [])
else:
    st.error("Pilih kelas terlebih dahulu!")

# Tampilkan soal sesuai kelas yang dipilih
if soal_list:
    st.write(f"Menampilkan soal untuk kelas {st.session_state.kelas}")
    for soal in soal_list:
        st.write(soal["soal"])

