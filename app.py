import streamlit as st
import os
from PIL import Image
from io import BytesIO
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.tavily import TavilyTools
from constants import SYSTEM_PROMPT, INSTRUCTIONS
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API")
GOOGLE_API_KEY = os.getenv('GEMINI_API')
MAX_IMAGE_WIDTH = 300

if not TAVILY_API_KEY:
    st.error("TAVILY_API_KEY not provided. Please set it as an environment variable.")
    st.stop()
if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not provided. Please set it as an environment variable.")
    st.stop()


@st.cache_data
def resize_image_for_display(image_file):
    """Resize image for display only, returns bytes"""
    try:
        if isinstance(image_file, str):
            img = Image.open(image_file)
        else:
            img = Image.open(image_file)
            image_file.seek(0)

        aspect_ratio = img.height / img.width
        new_height = int(MAX_IMAGE_WIDTH * aspect_ratio)
        img = img.resize((MAX_IMAGE_WIDTH, new_height), Image.Resampling.LANCZOS)

        buf = BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()
    except Exception as e:
        st.error(f"Error resizing image: {e}")
        return None


@st.cache_resource
def get_agent():
    return Agent(
        model=Gemini(id="gemini-2.0-flash-exp", api_key=GOOGLE_API_KEY),
        system_prompt=SYSTEM_PROMPT,
        instructions=INSTRUCTIONS,
        tools=[TavilyTools(api_key=TAVILY_API_KEY)],
        markdown=True,
    )

def analyze_image(image):
    agent = get_agent()
    with st.spinner('Analyzing image...'):
        try:
           response = agent.run(
                "Analyze the given image",
                images=[image],
            )
           st.markdown(response.content)
           st.success("Analysis completed successfully!")
        except Exception as e:
            st.error(f"Error analyzing image: {e}")
    st.session_state.analyze_clicked = True


def main():
    st.title("🔍 Product Ingredient Analyzer")
    st.write("Upload an image of a product's packaging or ingredient list to analyze its contents.")
    
    if 'selected_example' not in st.session_state:
        st.session_state.selected_example = None
    if 'analyze_clicked' not in st.session_state:
        st.session_state.analyze_clicked = False
    
    tab_examples, tab_upload, tab_camera = st.tabs([
        "📚 Example Products", 
        "📤 Upload Image", 
        "📸 Take Photo"
    ])
    
    with tab_examples:
        example_images = {
            "🍫 Chocolate Bar": "images/hide_and_seek.jpg",
            "🥤 Chocolate Drink": "images/bournvita.jpg",
            "🥔 Potato Chips": "images/lays.jpg",
            "🧴 Shampoo": "images/shampoo.jpg"
        }
        
        cols = st.columns(4)
        for idx, (name, path) in enumerate(example_images.items()):
            with cols[idx]:
                if st.button(name, use_container_width=True) and not st.session_state.analyze_clicked:
                    st.session_state.selected_example = path
                    st.session_state.analyze_clicked = False
    
    with tab_upload:
        uploaded_file = st.file_uploader(
            "Upload product image", 
            type=["jpg", "jpeg", "png"],
            help="Upload a clear image of the product's ingredient list"
        )
        if uploaded_file:
            resized_image = resize_image_for_display(uploaded_file)
            if resized_image:
                st.image(resized_image, caption="Uploaded Image", use_container_width=False, width=MAX_IMAGE_WIDTH)
                if st.button("🔍 Analyze Uploaded Image", key="analyze_upload") and not st.session_state.analyze_clicked:
                    analyze_image(uploaded_file)
    

    with tab_camera:
        camera_photo = st.camera_input("Take a picture of the product")
        if camera_photo:
            resized_image = resize_image_for_display(camera_photo)
            if resized_image:
                st.image(resized_image, caption="Captured Photo", use_container_width=False, width=MAX_IMAGE_WIDTH)
                if st.button("🔍 Analyze Captured Photo", key="analyze_camera") and not st.session_state.analyze_clicked:
                    analyze_image(camera_photo)
    
    if st.session_state.selected_example:
        st.divider()
        st.subheader("Selected Product")
        resized_image = resize_image_for_display(st.session_state.selected_example)
        if resized_image:
            st.image(resized_image, caption="Selected Example", use_container_width=False, width=MAX_IMAGE_WIDTH)
            if st.button("🔍 Analyze Example", key="analyze_example") and not st.session_state.analyze_clicked:
                analyze_image(st.session_state.selected_example)
                

if __name__ == "__main__":
    st.set_page_config(
        page_title="Product Ingredient Agent",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    main()