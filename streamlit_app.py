import streamlit as st
from controller import process_upload
import os
import model.config
st.set_page_config(
    page_title="Gym Equipment Detector",
    page_icon="🏋️",
    layout="wide"
)

# session init
if "current_view" not in st.session_state:
    st.session_state.current_view = "upload"
if "result_data" not in st.session_state:
    st.session_state.result_data = None
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None
#
# First Session
#
if st.session_state.current_view == "upload":

    st.markdown("<h1 style='text-align: center;'>🏋️ Gym Equipment Detector</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Upload an image of gym equipment to identify it.</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Gym Equipment Image", type=model.config.ALLOWED_EXTENSIONS)

    if uploaded_file is not None:
        # mini display for the uploaded image
        st.image(uploaded_file, width=300, caption="Ready to analyze")
        
        if st.button("🔍 Detect Equipment"):
            with st.spinner("Analyzing image..."):
                result = process_upload(uploaded_file)

            if result["status"] == "error":
                st.error(result["message"])
            elif result["status"] == "low_confidence":
                st.warning(f"{result['message']} (Confidence: {result['confidence']:.2f})")
            else:
                # preserve this session data in order for next session
                st.session_state.result_data = result
                st.session_state.uploaded_image = uploaded_file
                st.session_state.current_view = "result"
                st.rerun() # cause refresh for state switch

#
# Second Session
#
elif st.session_state.current_view == "result":
    # استرجاع الداتا من الـ State
    result = st.session_state.result_data
    uploaded_file = st.session_state.uploaded_image
    data = result["data"]

    st.markdown("<h1 style='text-align: center;'>🏋️ Detection Result</h1>", unsafe_allow_html=True)
    st.divider()

    # screen devide by columns
    col1, col2 = st.columns(2)

    
    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        st.success(f"Detected with {result['confidence']:.2f} confidence!")

        # button to get back to first session
        if st.button("⬅️ Analyze Another Image"):
            st.session_state.current_view = "upload"
            st.session_state.result_data = None
            st.session_state.uploaded_image = None
            st.rerun()


    with col2:
        st.markdown(f"### ⚙️ {data['equipment']}")
        st.markdown(f"**💪 Primary Target Muscle:** {data['primary_muscle']}")
        st.markdown(f"**📚 Exercise Info:** {data['academic_info']}")
        st.link_button("🎥 Watch Exercise Video", data["video_url"])
        if "visual" in data:
                    # git the absolute path so every time it is located dynamically
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    gif_path = os.path.join(base_dir, data["visual"])
                    
                    if os.path.exists(gif_path):
                        st.image(gif_path, width="content")
                    else:
                        st.error(f"Cannot find the Visual dataset in : {gif_path}")