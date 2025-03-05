from gtts import gTTS

def text_to_speech(text, language='en', output_file='outputs/output_audio.mp3'):
    tts = gTTS(text=text, lang=language)
    tts.save(output_file)
    print(f"Audio saved as {output_file}")
    return output_file
