def detect_emotion_from_text(text: str) -> dict:
    text = text.lower()

    # Basic keyword-based emotion detection
    if any(word in text for word in ["afraid", "fear", "scared", "nervous", "worried"]):
        emotion = "fear"
    elif any(word in text for word in ["angry", "frustrated", "furious", "annoyed"]):
        emotion = "anger"
    elif any(word in text for word in ["excited", "greedy", "overconfident", "rushed"]):
        emotion = "greed"
    elif any(word in text for word in ["calm", "relaxed", "confident", "steady"]):
        emotion = "calm"
    elif any(word in text for word in ["anxious", "tense", "stressed", "uncertain"]):
        emotion = "anxiety"
    else:
        emotion = "neutral"

    return {
        "label": emotion,
        "confidence": 0.8  # placeholder
    }

# ✅ Optional test
if __name__ == "__main__":
    user_input = input("🧠 How are you feeling about the market?\n> ")
    result = detect_emotion_from_text(user_input)
    print(f"\nDetected Emotion: {result['label'].upper()} ({result['confidence'] * 100}%)")
