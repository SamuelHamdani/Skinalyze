import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load model yang sudah dilatih
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("skinalyze-model.h5")

model = load_model()

# Label sesuai urutan kelas pada model kamu
labels = ['acne', 'dry', 'normal', 'oily']

# Mapping label ke bahasa Indonesia
label_mapping = {
    'acne': 'Berjerawat',
    'dry': 'Kering',
    'normal': 'Normal',
    'oily': 'Berminyak'
}

# Saran perawatan untuk setiap kondisi kulit
treatment_advice = {
    'acne': [
        "Cuci wajah dua kali sehari dengan pembersih lembut.",
        "Gunakan produk mengandung salicylic acid atau benzoyl peroxide.",
        "Hindari memencet jerawat.",
        "Gunakan pelembap non-komedogenik.",
        "Selalu gunakan sunscreen di pagi hari."
    ],
    'dry': [
        "Gunakan pembersih wajah tanpa sabun dan bebas alkohol.",
        "Gunakan pelembap dengan hyaluronic acid atau ceramide.",
        "Hindari mencuci wajah dengan air panas.",
        "Gunakan humidifier jika berada di ruangan ber-AC.",
        "Minum air putih yang cukup setiap hari."
    ],
    'oily': [
        "Gunakan pembersih wajah khusus kulit berminyak dua kali sehari.",
        "Gunakan pelembap ringan berbahan gel.",
        "Hindari mencuci wajah terlalu sering.",
        "Gunakan toner ringan dengan niacinamide.",
        "Gunakan kertas minyak jika wajah sangat berminyak."
    ],
    'normal': [
        "Kondisi Kulitmu sudah cukup bagus, lanjutkan rutinitas perawatan yang lembut dan seimbang."
    ]
}

# Judul aplikasi
st.markdown(
    "<h1 style='text-align: center;margin-bottom: 2rem; border-bottom: 2px solid #222; padding-bottom: 10px;'>Analisa Kulitmu</h1>",
    unsafe_allow_html=True
)
st.write("Unggah gambar wajah Anda untuk mendeteksi jenis masalah yang dialami (acne, kering, berminyak)")

# Upload file gambar
uploaded_file = st.file_uploader("Pilih gambar (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Tampilkan gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)

    # Tombol analisa
    if st.markdown(
                    """
                    <style>
                    .upload {
                        margin-top: 1rem;
                        padding:5px 15px; 
                        font-size:16px; 
                        border-radius: 10px;
                        border-color : #4DA1A9;
                        background-color: #fff;
                        color: #000;
                        cursor: pointer
                    }

                    .upload:hover {
                        background-color : #4DA1A9;
                        color : #fff;
                        transition: 0.3s ease;
                    }
                    </style>
                    <button class='upload'>Mulai Analisa</button></a>
                    """,unsafe_allow_html=True
                   ):
        # Preprocessing gambar
        img = image.resize((150, 150))
        img_array = np.array(img)
        if img_array.shape[-1] == 4:
            img_array = img_array[:, :, :3]
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Prediksi
        prediction = model.predict(img_array)
        predicted_class = labels[np.argmax(prediction)]
        translated_result = label_mapping[predicted_class]

        # Tampilkan hasil analisa
        st.success(f"Hasil Analisa Wajah : Kulit Anda **{translated_result}**")

        # Tampilkan saran perawatan
        st.markdown(
            "<h2 style='text-align: left; margin-bottom: 0.5rem;'>Saran Perawatan:</h2>",
            unsafe_allow_html=True
        )
        for advice in treatment_advice[predicted_class]:
            st.write(f"- {advice}")

st.markdown(
    """
    <style>
    .back {
        margin-top: 1rem;
        padding:5px 15px; 
        font-size:16px; 
        border-radius: 10px; 
        background-color: #fff;
        color: #000;
        cursor: pointer
    }

    .back:hover {
        background-color : #000;
        color : #fff;
        transition: 0.3s ease;
    }
    </style>
    <a href='https://www.skinalyze.my.id'>
    <button class='back'>Kembali</button></a>
    """,unsafe_allow_html=True
)