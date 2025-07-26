# Emotion-Detection-AI

---

````markdown
# 🧠 Emotion-Detection-AI

A simple Machine Learning CLI app that detects **emotions** from English text using Natural Language Processing (NLP) techniques.

## 📌 Features

- Predicts emotions like **joy**, **sadness**, **fear**, **anger**, etc.
- Built with Scikit-learn
- Command Line Interface (CLI) for easy use
- Trained using a labeled emotion dataset

## 🛠️ Requirements

Install the required Python packages:

```bash
pip install joblib scikit-learn
````

## 🚀 How to Run

1. Clone the repository or download the files:

   ```bash
   git clone https://github.com/YourUsername/Emotion-Detection-AI.git
   cd Emotion-Detection-AI
   ```

2. Make sure these files are present in the same folder:

   * `cli_emotion_detector.py`
   * `emotion_model.pkl`
   * `tfidf_vectorizer.pkl`

3. Run the CLI:

   ```bash
   python cli_emotion_detector.py
   ```

4. You’ll see a prompt:

   ```
   🧠 Welcome to the Emotion Detector!
   Type a sentence to predict its emotion. Press Enter to exit.
   ```

5. Type any sentence to detect emotion.

### ✅ Example:

```
Enter sentence: I'm so excited for the weekend!
🧠 Detected Emotion: joy
```

## 📁 File Structure

```
.
├── cli_emotion_detector.py     # Command line interface code
├── emotion_model.pkl           # Trained ML model
├── tfidf_vectorizer.pkl        # Fitted TF-IDF vectorizer
├── EDproject.ipynb             # Jupyter notebook (training & evaluation)
├── README.md                   # This file
```

## 👥 Contributing

Want to collaborate? Open a pull request or connect with [TechnikNest](https://techniknest.com)!

---

📌 **Submitted as part of the TechnikNest AI/ML Mini Project Series**
