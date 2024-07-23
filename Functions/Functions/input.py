import speech_recognition as sr

r = sr.Recognizer()

# ENTRADA
def listen():
    with sr.Microphone() as source:
        print("\nEsperando...")
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