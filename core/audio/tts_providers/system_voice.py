import pyttsx4

def tts_pyttsx3(text_chunk, location):
    engine = pyttsx4.init()
    engine.save_to_file(text_chunk,location)
    engine.runAndWait()
    engine.stop()

