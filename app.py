import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI đọc hóa đơn")

uploaded_file = st.file_uploader("Tải ảnh hóa đơn", type=["jpg","png","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Phân tích"):
        response = model.generate_content(
            ["Trích xuất thông tin hóa đơn gồm: Tên hàng, SL, Đơn giá, Thành tiền", image]
        )

        st.write(response.text)






