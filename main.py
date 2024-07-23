import functions as f

print("Olá, meu nome é Jarvis, como poderia tentar ajudá-lo hoje?")
user_input = f.understand()
if user_input == 'oi':
    print("Oi? Só oi? Isso foi meio simples demais...")

if user_input != None:
    print('\n', user_input)