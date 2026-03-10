import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Cấu hình nhanh
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner")

uploaded_file = st.file_uploader("Tải ảnh hóa đơn...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ảnh đã tải lên', use_container_width=True)
    
    if st.button("🚀 Phân tích ngay"):
        with st.spinner('AI đang tính toán...'):
            try:
                # Prompt cực ngắn để AI phản hồi nhanh nhất có thể
                prompt = "Đọc thực phẩm từ ảnh này và gợi ý 3 bữa ăn tiết kiệm cho sinh viên. Trả lời ngắn bằng tiếng Việt."
                response = model.generate_content([prompt, image])
                st.success("Xong rồi!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Lỗi: {e}")


