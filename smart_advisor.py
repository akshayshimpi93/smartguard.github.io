# smart_advisor.py

def get_coaching_tip(emotion):
    tips = {
        "Happy": "Maintain focus and avoid overconfidence.",
        "Sad": "Take a break or review your recent losses calmly.",
        "Angry": "Step away from trading until you're calm.",
        "Surprised": "Avoid making impulsive decisions.",
        "Neutral": "Great! Stay objective and stick to your plan.",
        "Fear": "Don't let fear prevent smart opportunities. Reassess risk.",
        "Disgust": "Reflect — are you trading emotionally? Adjust your mindset."
    }
    return tips.get(emotion, "Stay focused and stick to your strategy.")
