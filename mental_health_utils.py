from transformers import pipeline

# Load Hugging Face sentiment-analysis pipeline
classifier = pipeline("sentiment-analysis")

def analyze_mental_state(text):
    result = classifier(text)[0]
    label = result['label'].lower()
    score = result['score']

    if label == "negative":
        recommendation = """
- 💬 Consider speaking with a trusted friend, counselor, or therapist.
- 🧘 Practice deep breathing, yoga, or mindfulness meditation regularly.
- 📔 Write your thoughts in a journal to gain clarity and reduce stress.
- 🛌 Ensure you're getting enough restful sleep every night.
- 🏃‍♂️ Engage in physical activities like walking, dancing, or light workouts.
- 🍎 Eat well-balanced meals and avoid excessive caffeine or alcohol.
- 📱 Limit social media use and try digital detox to avoid comparison fatigue.
"""
    else:
        recommendation = """
- 🌞 Keep a gratitude journal to reflect on positive moments daily.
- 🚶‍♀️ Maintain regular physical activity and spend time outdoors.
- 🍽️ Eat nutritious meals to fuel your energy and mood.
- 💬 Stay socially connected with friends, family, or support groups.
- 😴 Get 7–9 hours of quality sleep every night to support mental wellness.
- 🎨 Pursue creative hobbies or passions that bring you joy.
- 🎯 Set small achievable goals to stay motivated and inspired.
"""

    return label, score, recommendation
