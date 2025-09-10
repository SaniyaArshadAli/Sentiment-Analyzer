# Sentiment-Analyzer

Welcome to the **Awesome Sentiment Analyzer**!  
This is a simple, yet elegant web application built with **Python** and **Flask** that allows you to analyze the sentiment of any text you provide. Whether you want to check if a sentence is **positive, negative, or neutral**, this tool will give you a quick and accurate breakdown.

---

## 🌟 Features
- ⚡ **Real-time Analysis**: Get instant sentiment analysis results.  
- 📊 **Detailed Metrics**: View polarity and subjectivity scores for a deeper understanding of the sentiment.  
- 🎨 **Modern UI**: A clean, responsive user interface with a sleek design, powered by **Tailwind CSS**.  
- 🖊️ **Easy to Use**: Simply type or paste your text and click a button.  

---

## 🚀 Installation

Follow these steps to set up the project locally.

### ✅ Prerequisites
- Python 3.6+  
- `pip` (Python package installer)  

### 📂 Project Structure
sentiment-analyzer/
├── app.py
└── templates/
└── index.html
sentiment-analyzer/
├── app.py
└── templates/
└── index.html

### 📥 Step-by-Step Guide
1. **Clone the Repository (if applicable)** or set up the files as shown above.  

2. **Install Required Libraries**  
   ```bash
   pip install Flask textblob
   ```
3. Download TextBlob's Corpora
```
python -m textblob.download_corpora
```
4. Run the Application
```
python app.py
```
5. Access the App
Open your browser and go to:
👉 http://127.0.0.1:5000/

📋 Usage
Open the application in your browser.

Type or paste the text you want to analyze into the text box.

Click the "Analyze Sentiment" button.

View the results:

Sentiment classification (Positive / Negative / Neutral)

Polarity score (range: -1 to 1)

Subjectivity score (range: 0 to 1)

💻 Technologies Used
Backend: Python, Flask

Sentiment Analysis: TextBlob

Frontend: HTML, Tailwind CSS

✨ Built with ❤️ using Flask & TextBlob
