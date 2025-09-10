from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment_result = None
    if request.method == 'POST':
        user_text = request.form['user_text']
        # Perform sentiment analysis using TextBlob
        analysis = TextBlob(user_text)

        # Polarity score ranges from -1.0 (very negative) to 1.0 (very positive)
        polarity = analysis.sentiment.polarity
        # Subjectivity score ranges from 0.0 (very objective) to 1.0 (very subjective)
        subjectivity = analysis.sentiment.subjectivity

        # Classify sentiment based on polarity score
        if polarity > 0:
            sentiment_class = "Positive 😃"
        elif polarity < 0:
            sentiment_class = "Negative 😠"
        else:
            sentiment_class = "Neutral 😐"

        sentiment_result = {
            'text': user_text,
            'sentiment': sentiment_class,
            'polarity': polarity,
            'subjectivity': subjectivity
        }
    
    return render_template('index.html', sentiment_result=sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)