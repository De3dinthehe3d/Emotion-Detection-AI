import joblib

model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("\n🧠 Welcome to the Emotion Detector!")
print("Type a sentence to predict its emotion. Press Enter to exit.\n")

while True:
    text = input("Enter sentence: ").strip()
    if not text:
        print("Goodbye! 👋")
        break

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    print(f"🧠 Detected Emotion: {prediction}\n")
