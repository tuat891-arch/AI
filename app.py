import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Cấu hình thẳng từ Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner")
st.write("Dự án hỗ trợ sinh viên lên thực đơn tiết kiệm")

file = st.file_uploader("Tải ảnh hóa đơn...", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption='Ảnh đã tải', use_container_width=True)
    
    if st.button("🚀 Gợi ý món ăn ngay"):
        with st.spinner('Đang tính toán...'):
            try:
                # Câu lệnh siêu ngắn để AI phản hồi nhanh
                prompt = "Liệt kê thực phẩm và gợi ý 3 món ăn sinh viên tiết kiệm. Trả lời ngắn gọn bằng tiếng Việt."
                response = model.generate_content([prompt, img])
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Lỗi: {e}")

