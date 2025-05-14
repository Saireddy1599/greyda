
from flask import Flask, render_template
import pandas as pd
from textblob import TextBlob
import os

app = Flask(__name__)

@app.route('/chart')
def chart():
    csv_file = os.path.join(os.path.dirname(__file__), 'boat_airdopes_161_reviews.csv')
    df = pd.read_csv(csv_file)

    df['polarity'] = df['review'].apply(lambda text: TextBlob(str(text)).sentiment.polarity)

    positive = (df['polarity'] > 0).sum()
    negative = (df['polarity'] < 0).sum()
    neutral = (df['polarity'] == 0).sum()
    total = positive + negative + neutral

    pos_pct = round(positive / total * 100, 2)
    neg_pct = round(-negative / total * 100, 2)  # negative % shown as negative bar
    neu_pct = round(neutral / total * 100, 2)

    return render_template('chart.html', pos_pct=pos_pct, neg_pct=neg_pct, neu_pct=neu_pct)

if __name__ == '__main__':
    app.run(debug=True)
