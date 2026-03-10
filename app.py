import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Cấu hình API Key (Lấy từ Secrets)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Chưa cấu hình API Key trong mục Secrets!")

model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner")
st.write("Hỗ trợ sinh viên quản lý thực đơn tiết kiệm")

uploaded_file = st.file_uploader("Tải lên ảnh hóa đơn (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Hóa đơn đã tải lên', use_container_width=True)
    
    if st.button("Phân tích & Gợi ý món ăn"):
        with st.spinner('AI đang suy nghĩ...'):
            try:
                # Câu lệnh ngắn gọn để chạy nhanh hơn
                prompt = "Liệt kê thực phẩm trong ảnh và gợi ý 3 món ăn sinh viên tiết kiệm. Trả lời ngắn bằng tiếng Việt."
                
                # Gọi AI xử lý ảnh
                response = model.generate_content([prompt, image])
                
                st.success("Xong rồi!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Lỗi: {e}")

