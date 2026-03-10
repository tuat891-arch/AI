import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Cấu hình API Key (Dán cái mã bạn vừa copy vào giữa dấu ngoặc kép)
genai.configure(api_key="DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY")

# 2. Thiết lập mô hình AI
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Giao diện ứng dụng
st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner - AI")
st.subheader("Hỗ trợ sinh viên quản lý thực đơn tiết kiệm")

st.sidebar.header("Hướng dẫn")
st.sidebar.info("Chụp ảnh hóa đơn đi chợ của bạn, AI sẽ giúp bạn lên thực đơn!")

uploaded_file = st.file_uploader("Tải lên ảnh hóa đơn (JPG, PNG)...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Hóa đơn đã tải lên', use_container_width=True)
    
    if st.button("Phân tích & Gợi ý món ăn"):
        with st.spinner('AI đang suy nghĩ...'):
            try:
                # Gửi ảnh và câu lệnh cho Gemini
            # Thay đoạn prompt cũ bằng đoạn ngắn gọn này:
prompt = "Liệt kê thực phẩm trong ảnh và gợi ý 3 món ăn sinh viên tiết kiệm. Trả lời ngắn gọn bằng tiếng Việt."
                response = model.generate_content([prompt, image])
                
                st.success("Xong rồi!")
                st.markdown(response.text)
            except Exception as e:

                st.error(f"Có lỗi xảy ra: {e}")
