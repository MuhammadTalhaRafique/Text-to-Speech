from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    try:
        data = request.json
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Convert text to speech
        speech = gTTS(text=text, lang='ur', slow=False)
        speech.save("static/voice.mp3")

        return jsonify({"audio_url": "/static/voice.mp3"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
