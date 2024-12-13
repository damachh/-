import telebot

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Как тебя зовут?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    name = message.text
    bot.send_message(message.chat.id, f'Приятно  познакомиться, {name}! Сколько тебе лет?')
    bot.register_next_step_handler(message, calculate_birth_year)

def calculate_birth_year(message):
    try:
        age = int(message.text)
        current_year = 2024
        birth_year = current_year - age
        bot.send_message(message.chat.id, f"Ты родился в {birth_year} году.")
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите число.')
        bot.register_next_step_handler(message, calculate_birth_year)

bot.polling(none_stop=True)