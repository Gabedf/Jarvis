from Functions import main as f
from Data import options as op

print("Olá, meu nome é Jarvis, como poderia tentar ajudá-lo hoje?\n")
f.firstOptions()
user_input = input("'Digite o que deseja: ")

while user_input.strip().lower() != 'sair':
    if user_input.strip().lower() == 'hora':
        time =  f.get_current_time()
        print(f'Agora são {time} horas.')
    elif user_input.strip().lower() == 'clima':
        print(f"O clima está {f.climate()} graus.")
    elif user_input.strip().lower() == 'cotação':
        f.price()
    elif user_input.strip().lower() == 'conversa':
        print('Sobre o que você gostaria de conversar? ')
        f.talkOptions()
        user_input = input("'Digite o que deseja: ")
        if user_input.strip().lower() == 'piada':
            print(f.jokesOptions())
        elif user_input.strip().lower() == 'curiosidade':
            print(f.curiositiesOptions())
        else:
            print('Opção não encontrada.')
    else:
        print('Opção não encontrada.')

    print("\nCom o que mais eu poderia te ajudar?\n")
    f.firstOptions()
    user_input = input("'Digite o que deseja: ")
