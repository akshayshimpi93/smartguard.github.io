import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import numpy as np
import pandas as pd
from datetime import datetime

# Simple mock logic to classify emotion from face bounding box (for testing/demo)
def mock_detect_emotion():
    import random
    emotions = ['happy', 'sad', 'angry', 'surprise', 'neutral']
    return random.choice(emotions)

# Start webcam
cap = cv2.VideoCapture(0)

print("📸 Press 'q' to capture and analyze mock emotion")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error accessing webcam")
        break

    bbox, label, conf = cv.detect_common_objects(frame)
    out = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("SmartGuard (Press 'q' to analyze)", out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        emotion = mock_detect_emotion()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save result
        df = pd.DataFrame([{"Timestamp": timestamp, "Dominant Emotion": emotion}])
        df.to_csv("emotion_log.csv", mode='a', header=not pd.io.common.file_exists("emotion_log.csv"), index=False)

        print(f"✅ Emotion Detection Complete")
        print(f"🕒 Timestamp: {timestamp}")
        print(f"😀 Detected Emotion: {emotion}")
        input("🔚 Press Enter to exit...")
        break

cap.release()
cv2.destroyAllWindows()
