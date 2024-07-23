import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Esperando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return audio

def understand():
    try:
        audio = listen()
        text = r.recognize_google(audio, language="pt-BR")
        return text
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
    except sr.RequestError:
        print("Não foi possível acessar o serviço de reconhecimento de fala. Verifique sua conexão com a internet.")
    return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
