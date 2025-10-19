import streamlit as st
import cv2
import numpy as np
import tempfile
from PIL import Image
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="SmartGuard AI", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        .reportview-container {
            background: #f9f9f9;
        }
        .sidebar .sidebar-content {
            background: #e6f2ff;
        }
        h1 {
            text-align: center;
            font-size: 3.5em;
            background: linear-gradient(to right, #ff416c, #ff4b2b);
            -webkit-background-clip: text;
            color: transparent;
        }
        footer {
            text-align: center;
            padding: 10px;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
    <h1>🧠 SmartGuard AI - Emotion & Face Tracker</h1>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.title("🧭 Navigation")
selected_tool = st.sidebar.radio("Choose a Feature", ["😄 Emotion Detection", "👤 Face Detection"])
st.sidebar.markdown("---")
st.sidebar.markdown("✅ Select a feature and press the button to activate webcam.")
st.sidebar.markdown("🔒 Your data stays private!")

# ---------- Webcam Capture ----------
def capture_from_webcam(filename="capture.jpg"):
    st.info("📸 Your webcam will open. Press 'q' to capture.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("❌ Could not access the webcam.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam - Press 'q' to Capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            filepath = os.path.join(tempfile.gettempdir(), filename)
            cv2.imwrite(filepath, frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return filepath if os.path.exists(filepath) else None

# ---------- Emotion Detection ----------
if selected_tool == "😄 Emotion Detection":
    st.subheader("🎭 Emotion Detection")
    if st.button("Start Emotion Detection"):
        img_path = capture_from_webcam("emotion.jpg")
        if img_path:
            img = Image.open(img_path)
            st.image(img, caption="🖼️ Captured Frame", use_column_width=True)

            # Simulated Emotion Result
            emotion = np.random.choice(["Happy 😊", "Sad 😢", "Angry 😠", "Neutral 😐"])
            st.success(f"🧠 Detected Emotion: **{emotion}**")

            # Dummy emotion data
            labels = ["Happy", "Sad", "Angry", "Neutral"]
            values = np.random.randint(5, 30, size=4)

            # Charts Layout
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### 📊 Emotion Distribution")
                fig1, ax1 = plt.subplots(figsize=(4, 4))
                ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90,
                        colors=["#FF9999", "#99CCFF", "#FFB266", "#CCCCCC"])
                ax1.axis('equal')
                st.pyplot(fig1)

            with col2:
                st.markdown("### 📈 Emotion Intensity")
                fig2, ax2 = plt.subplots(figsize=(4, 4))
                ax2.bar(labels, values, color=["#FF9999", "#99CCFF", "#FFB266", "#CCCCCC"])
                ax2.set_ylabel("Count")
                ax2.set_title("Emotion Intensity Levels")
                st.pyplot(fig2)

# ---------- Face Detection ----------
elif selected_tool == "👤 Face Detection":
    st.subheader("👁️ Face Detection")
    if st.button("Start Face Detection"):
        img_path = capture_from_webcam("face.jpg")
        if img_path:
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            st.success(f"🧑‍🤝‍🧑 Detected {len(faces)} face(s)")
            st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)

# ---------- Footer ----------
st.markdown("""<hr style="margin-top: 40px;">""", unsafe_allow_html=True)
st.markdown("""
    <footer>
        🚀 Made with ❤️ by <strong>Akshay Shimpi</strong> | © 2025 SmartGuard AI
    </footer>
""", unsafe_allow_html=True)
