import streamlit as st
import requests

# ---------------------------------------------------------
# CHANGE THIS if your backend runs somewhere else
# (e.g. after deploying to Render, replace with the live URL)
# ---------------------------------------------------------
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Gym Equipment Detector",
    page_icon="🏋️",
    layout="centered"
)

st.title("🏋️ Gym Equipment Detector")

st.write(
    "Upload an image of gym equipment to identify it and view its information."
)

uploaded_file = st.file_uploader(
    "Upload Gym Equipment Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Detect Equipment"):

        with st.spinner("Analyzing image..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post(f"{BACKEND_URL}/predict", files=files, timeout=15)

            except requests.exceptions.ConnectionError:
                st.error(
                    "Couldn't reach the backend. Make sure it's running "
                    f"at {BACKEND_URL} (uvicorn app.main:app --reload)."
                )
                st.stop()

        if response.status_code != 200:
            st.error(f"Backend error: {response.json().get('detail', 'Unknown error')}")
            st.stop()

        result = response.json()

        if result["status"] == "low_confidence":
            st.warning(
                f"{result['message']} (confidence: {result['confidence']:.0%})"
            )
            st.stop()

        equipment_data = result["data"]

        st.success(f"Detected with {result['confidence']:.0%} confidence!")

        st.divider()

        st.subheader("🏋️ Equipment")
        st.write(equipment_data["equipment"])

        st.subheader("💪 Primary Target Muscle")
        st.write(equipment_data["primary_muscle"])

        st.subheader("📚 Exercise Information")
        st.write(equipment_data["academic_info"])

        st.subheader("🎥 Exercise Video")
        st.link_button(
            "Watch Exercise Video",
            equipment_data["video_url"]
        )