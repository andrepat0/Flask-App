from flask import Flask,request, jsonify
from sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
