import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não entendi o que você disse")
    except sr.RequestError:
        print("Não foi possível conectar ao serviço de reconhecimento de voz")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Olá, meu nome é Jarvis, como poderia tentar ajudá-lo hoje?")
    user_input = listen()
    if user_input:
        speak(f"Você disse: {user_input}")
