import streamlit as st
import google.generativeai as genai
from PIL import Image

# Kiểm tra API key
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Thiếu GEMINI_API_KEY")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={
        "temperature": 0.4,
        "max_output_tokens": 300
    }
)

st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner")

uploaded_file = st.file_uploader("Tải ảnh hóa đơn / thực phẩm", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🚀 Phân tích ngay"):
        with st.spinner("AI đang phân tích..."):
            try:
                prompt = """
                Nhìn vào ảnh thực phẩm này.
                1. Liệt kê thực phẩm có trong ảnh
                2. Gợi ý 3 bữa ăn tiết kiệm cho sinh viên
                Trả lời ngắn gọn bằng tiếng Việt.
                """

                response = model.generate_content([prompt, image])

                st.success("Xong!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Lỗi: {e}")



