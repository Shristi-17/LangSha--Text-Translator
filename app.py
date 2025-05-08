from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Function to detect language
def detect_language(text):
    translator = Translator()
    detected = translator.detect(text)
    return detected.lang

# Function to translate text
def translate_text(text, target_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

# Function to show supported languages
def show_supported_languages():
    languages = [
        "af", "am", "ar", "bn", "bs", "ca", "cs", "cy", "da", "de", "el", "en", "eo", "es", "et", "fa",
        "fi", "fr", "ga", "gl", "gu", "he", "hi", "hr", "ht", "hu", "hy", "id", "is", "it", "ja", "jv",
        "ka", "km", "kn", "ko", "la", "lt", "lv", "mk", "ml", "mr", "ms", "mt", "ne", "nl", "pl", "ps",
        "pt", "ro", "ru", "si", "sk", "sl", "sq", "sr", "sv", "sw", "ta", "te", "th", "tr", "uk", "ur",
        "vi", "xh", "zh", "zu"
    ]
    # Create a dictionary to pass languages in 4 columns for easy rendering
    num_cols = 8
    num_rows = len(languages) // num_cols + (len(languages) % num_cols > 0)

    language_columns = []
    for i in range(num_rows):
        row = [languages[i + j * num_rows] if i + j * num_rows < len(languages) else "" for j in range(num_cols)]
        language_columns.append(row)

    return language_columns

# Route for homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        target_lang = request.form['target_lang']
        
        if input_text and target_lang:
            # Detect language and translate text
            detected_language = detect_language(input_text)
            translated_text = translate_text(input_text, target_lang)
            return render_template('index.html', detected_language=detected_language, translated_text=translated_text)
        else:
            return render_template('index.html', error="Please provide both text and target language code.")
    
    return render_template('index.html', language_columns=show_supported_languages())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





