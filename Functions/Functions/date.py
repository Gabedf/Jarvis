import datetime

# DATA E HORA
def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M")  # Formata a hora como HH:MM
    return current_time