# 🏋️ Project-IronSight

Project IronSight is an AI-powered web application designed to act as a digital assistant for gym-goers. By simply uploading an image of any gym machine, the application identifies the equipment and provides comprehensive biomechanical and academic information, including the primary targeted muscle, correct form instructions, and visual demonstrations.

## ✨ Features
* 🤖 **Dual-Model Inference:** Utilizes two independently trained YOLO models simultaneously to ensure high confidence and compare detection accuracy.
* ⚡ **Interactive UI:** Built with Streamlit, featuring a custom dark-themed gradient for a sleek, gym-appropriate aesthetic.
* 🧠 **Smart Data Aggregation:** Dynamically fetches academic exercise info, muscle targeting, and external video links.
* 🎞️ **Synchronized Visuals:** Displays animated GIFs demonstrating proper form side-by-side with the user's uploaded image.

## 🗂️ The Dataset
This project is trained and evaluated using the **Bangkit Dataset of Gym Equipment Object Detection**. 
You can explore the dataset and its annotations on Roboflow (Link provided in project resources).

## 🚀 How to Download & Run
1. **Clone the repository:**
   ```bash
   git clone [Your GitHub Repo Link]
   cd Project-IronSight
   ```
2. **Install the dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Fire it up:**
   ```bash
   streamlit run streamlit_app.py
   ```

## 🎮 How to Use It
1. Open the local Streamlit URL in your browser.
2. Snap a photo of a machine at the gym or upload one from your gallery.
3. Click the detection button.
4. The AI will instantly highlight the machine, give you its name, show you the primary target muscle, and display personal form tips along with a guiding GIF.

## 🔮 Future Work
* **Multi-Machine Vision:** Enhancing the detection logic to identify and label multiple gym machines in a single wide-angle shot.
* **Dual-Model Face-Off:** Expanding the UI to dynamically compare predictions from different YOLO iterations to find the absolute best match.
* **History & Tracking:** Adding a feature to save your scanned machines so you can automatically build a workout routine based on the equipment you interacted with.
