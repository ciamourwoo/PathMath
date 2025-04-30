# ===== Halaman SOAL =====
if st.session_state["halaman"] == "soal":
    st.title(f"🧠 Materi: {st.session_state['materi']} | Level: {st.session_state['level']}")
    st.write(f"Halo {st.session_state['nama']}! Yuk kita lanjut petualanganmu di level ini!")

    materi = st.session_state["materi"]
    level = st.session_state["level"]

    soal, jawaban_benar, penjelasan = soal_bank[materi][level]
    st.subheader(f"🎯 Soal Level {level}")
    st.write(soal)

    jawaban_user = st.text_input("Jawabanmu apa nih?", key=f"jawaban_{materi}_{level}")

    if st.button("🚀 Kirim Jawaban"):
        if jawaban_user.strip() == jawaban_benar:
            st.success("🎉 Keren! Jawabanmu benar!")
            if level == 3:
                st.session_state["game_selesai"] = True
                st.session_state["halaman"] = "selesai"
            else:
                st.session_state["level"] = min(3, level + 1)
                st.rerun()
        else:
            st.error("😅 Wah, masih belum tepat nih.")
            st.info(f"🧩 Petunjuk: {penjelasan}")

    st.markdown("---")
    if st.button("🏠 Kembali ke Halaman Utama"):
        st.session_state["halaman"] = "identitas"
        st.session_state["level"] = 1
        st.session_state["nomor_soal"] = 1
        st.session_state["game_selesai"] = False
        st.session_state["nama"] = ""
        st.rerun()
