from Functions import main as f

print("Olá, meu nome é Jarvis, como poderia tentar ajudá-lo hoje?")
f.firstOptions()
user_input = f.understand()

while user_input.lower() != 'sair':
    print("Com o que mais eu poderia te ajudar?")
    f.firstOptions()
    user_input = f.understand()

if user_input == 'oi':
    print("Oi? Só oi? Isso foi meio simples demais...")

if user_input != None:
    print('\n', user_input)