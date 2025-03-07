# Flask Text-to-Speech (TTS) App

This is a simple **Text-to-Speech (TTS)** web application built using **Flask**, **Google Text-to-Speech (gTTS)**, **HTML**, **CSS**, and **JavaScript**. The app allows users to enter text, convert it into speech (Urdu supported), and play/download the generated audio file.

## Features
✔ Convert **Urdu text** into speech using gTTS  
✔ Simple and responsive **web UI**  
✔ Play generated audio in the browser  
✔ Flask backend with REST API  

## Project Structure
```
/text-to-speech-app
│── app.py                # Flask backend
│── Text.txt              # Sample text file (optional)
│── templates/
│   └── index.html        # Frontend UI
│── static/
│   ├── styles.css        # Styling
│   └── script.js         # JavaScript logic
```

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/MuhammadTalhaRafique/text-to-speech-app.git
cd text-to-speech-app
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

## Usage
### 1. Run the Flask App
```bash
python app.py
```

### 2. Open in Browser
Go to `http://127.0.0.1:5000/` in your web browser.

### 3. Enter Text & Convert to Speech
- Enter any text in the textarea.
- Click the **Convert to Speech** button.
- The generated speech will be played automatically.

## API Endpoint
### `POST /speak`
Converts text to speech and returns the generated audio file.
#### **Request Body (JSON):**
```json
{
    "text": "آپ کیسے ہیں؟"
}
```
#### **Response (JSON):**
```json
{
    "audio_url": "/static/voice.mp3"
}
```

## Dependencies
- Flask
- gTTS (Google Text-to-Speech)

