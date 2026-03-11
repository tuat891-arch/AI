import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash-latest")

st.title("Phân tích hóa đơn")

uploaded_file = st.file_uploader("Tải ảnh hóa đơn", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Phân tích"):
        response = model.generate_content(
            ["Trích xuất thông tin hóa đơn", image]
        )
        st.write(response.text)





