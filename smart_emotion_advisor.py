from deepface import DeepFace
import cv2
import datetime
import csv

# Coaching logic
def generate_advice(emotion):
    tips = {
        "happy": "Stick to your strategy — don't let overconfidence creep in!",
        "sad": "Take a break and reset. Emotional trades are risky.",
        "angry": "Cool down. Avoid making decisions while angry.",
        "fear": "Stay calm and follow your plan — don't panic sell.",
        "surprise": "Pause and evaluate. Don’t react too fast.",
        "disgust": "Detach emotions from decisions. Review objectively.",
        "neutral": "You’re focused — great state for decision making."
    }
    return tips.get(emotion.lower(), "Stay self-aware and emotionally balanced.")

# Setup
cap = cv2.VideoCapture(0)
csv_file = open("emotion_log.csv", mode="a", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Timestamp", "Dominant Emotion"])

print("Press 'q' to quit...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Webcam error. Exiting...")
        break

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        advice = generate_advice(emotion)

        # Show emotion and advice on video
        cv2.putText(frame, f"Emotion: {emotion}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.putText(frame, f"Advice: {advice}", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Log to CSV
        csv_writer.writerow([timestamp, emotion])
        csv_file.flush()

    except Exception as e:
        print("Error:", e)

    # Show webcam feed
    cv2.imshow("SmartCoach AI - Emotion + Advice", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
csv_file.close()
