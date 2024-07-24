from Functions import main as f
from Data import options as op

f.speak("Olá, meu nome é Jarvis, como poderia tentar ajudá-lo hoje?\n")
f.firstOptions()
user_input = f.understand()

while user_input != 'sair':
    if user_input == 'hora':
        time =  f.get_current_time()
        f.speak(f'Agora são {time} horas.')
    elif user_input == 'conversa':
        f.speak('Sobre o que você gostaria de conversar? ')
        f.talkOptions()
        user_input = f.understand()
        if user_input == 'piada':
            f.speak(f.jokesOptions())
        elif user_input == 'curiosidade':
            f.speak(f.curiositiesOptions())
        else:
            f.speak('Opção não encontrada.')
    else:
        f.speak('Opção não encontrada.')

    f.speak("\nCom o que mais eu poderia te ajudar?\n")
    f.firstOptions()
    user_input = f.understand()
