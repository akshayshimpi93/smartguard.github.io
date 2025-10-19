import csv

# Simple logic to generate coaching tips based on emotions
def generate_tip(emotion):
    tips = {
        "angry": "Take a deep breath. Step away from the screen and refocus before making decisions.",
        "sad": "It's okay to feel low. Avoid trading in emotional states. Take a short break.",
        "happy": "Great! Just make sure your excitement doesn’t lead to impulsive decisions.",
        "neutral": "You're calm and balanced — a good time to make logical decisions.",
        "fear": "Don’t let fear control your trades. Reassess risk and avoid panic selling.",
        "disgust": "Your discomfort may cloud judgment. Avoid trading until you feel better.",
        "surprise": "Unexpected events? Re-evaluate your position with a clear head."
    }
    return tips.get(emotion.lower(), "Stay aware of your emotional state before trading.")

# Read last emotion from CSV
def get_latest_emotion(csv_file):
    try:
        with open(csv_file, 'r') as file:
            reader = list(csv.reader(file))
            if len(reader) > 1:
                last_row = reader[-1]
                return last_row[1]  # Emotion column
            else:
                return None
    except Exception as e:
        print("Error reading CSV:", e)
        return None

# Main logic
csv_path = "emotion_log.csv"
emotion = get_latest_emotion(csv_path)

if emotion:
    print(f"\n🧠 Last Detected Emotion: {emotion}")
    tip = generate_tip(emotion)
    print(f"\n💡 SmartCoach Tip:\n{tip}")
else:
    print("⚠️ No emotion data found. Please run emotion detection or use a valid CSV.")
