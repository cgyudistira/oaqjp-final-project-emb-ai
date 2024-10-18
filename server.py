"""
Module to handle the server side of the emotion detection application.

This module sets up a Flask server to receive text input and return emotion analysis.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Route to detect emotions from the provided text.

    Returns:
        JSON response containing emotion analysis or error message.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
