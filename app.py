import streamlit as st
import google.generativeai as genai
from PIL import Image

# Kiểm tra API key
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Thiếu GEMINI_API_KEY trong Secrets")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model nhanh
model = genai.GenerativeModel("gemini-1.5-flash")

# Giao diện
st.set_page_config(page_title="Smart Meal Planner", page_icon="🥗")
st.title("🥗 Smart Meal Planner")

uploaded_file = st.file_uploader(
    "Tải ảnh hóa đơn / thực phẩm", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    # mở ảnh
    image = Image.open(uploaded_file).convert("RGB")

    # giảm kích thước ảnh để xử lý nhanh
    image.thumbnail((800, 800))

    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

    if st.button("🚀 Phân tích ngay"):

        with st.spinner("AI đang phân tích..."):

            try:

                prompt = """
                Đọc nội dung hóa đơn trong ảnh và liệt kê:

                - Tên sản phẩm
                - Số lượng
                - Đơn giá
                - Thành tiền

                Trả lời ngắn gọn bằng tiếng Việt.
                """

                response = model.generate_content([prompt, image])

                st.success("Phân tích xong!")
                st.write(response.text)

            except Exception as e:
                st.error(f"Lỗi: {e}")




