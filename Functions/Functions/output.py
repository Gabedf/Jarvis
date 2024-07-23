import pyttsx3

# SAÍDA
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
