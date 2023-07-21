import streamlit as st
import pickle

# load model
model = pickle.load(open("heart_model.sav", "rb"))

# judul halaman
st.title("Prediksi Penyakit Jantung")

# membuat kolom
col1, col2, col3 = st.columns(3)

# membuat form imputan user
with col1:
    age = st.number_input("Umur")

with col2:
    sex = st.number_input("Jenis Kelamin")

with col3:
    cp = st.number_input("Jenis Nyeri Dada")

with col1:
    trestbps = st.number_input("Tekanan Darah")

with col2:
    chol = st.number_input("Kadar Kolesterol")

with col3:
    fbs = st.number_input("Gula Darah")

with col1:
    restecg = st.number_input("Elektrokardiografi")

with col2:
    thalach = st.number_input("Deteak Jantung Maksimum")

with col3:
    exang = st.number_input("Induksi Angina")

with col1:
    oldpeak = st.number_input("ST Depression")

with col2:
    slope = st.number_input("Slope")

with col3:
    ca = st.number_input("Pembuluh Darah")

with col1:
    thal = st.number_input("Nilai Thal")

# inisialisasi prediksi
heart_diag = ""

# tombol prediksi
if st.button("Prediksi Penyakit Jantung"):
    heart_predict = model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    if (heart_predict[0] == 1):
        heart_diag = "Pasien Terdiagnosa Penyakit Jantung"
    else:
        heart_diag = "Pasien Tidak Terdiagnosa Penyakit Jantung"

st.success(heart_diag)
