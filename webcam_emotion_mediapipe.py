import cv2
import mediapipe as mp
import pandas as pd
import numpy as np
from datetime import datetime
import random
import os

# Initialize Mediapipe face detector
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# List of mock emotions
emotions = ['Happy', 'Sad', 'Angry', 'Surprised', 'Neutral']

# Start webcam
cap = cv2.VideoCapture(0)
print("📸 Webcam started. Press 'q' to capture emotion.")

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.6) as face_detection:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error: Could not access webcam.")
            break

        # Convert to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)

        cv2.imshow('SmartGuard Webcam (press q)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            if results.detections:
                print("✅ Face detected.")

                # Use mock prediction for now
                predicted_emotion = random.choice(emotions)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Log to CSV
                df = pd.DataFrame([{
                    "Timestamp": timestamp,
                    "Dominant Emotion": predicted_emotion
                }])
                df.to_csv("emotion_log.csv", mode='a', header=not os.path.exists("emotion_log.csv"), index=False)

                print(f"🧠 Emotion logged: {predicted_emotion}")
            else:
                print("❌ No face detected. Try again.")
            break

cap.release()
cv2.destroyAllWindows()
