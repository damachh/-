import telebot

bot = telebot.TeleBot('7304500465:AAFXdZtysg1HEHo-lvZs__CWmDl2S6JARz8')

@bot.message_handler(func=lambda message: True)

def start(message):
    bot.send_message(message.chat.id, 'Привет.Как тебя зовут?')
    bot.register_next_step_handler(message, get_username)

def get_username(message):
    name=message.text
    bot.send_message(message.chat.id, f'А как твоя фамилия, {name}?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    nam=message.text
    bot.send_message(message.chat.id, f'Приятно Познакомиться, бро!Сколько тебе лет?')
    bot.register_next_step_handler(message,calculate_birth_year)

def calculate_birth_year(message):
    try:
        age = int(message.text)
        current_year=2024
        birth_year = current_year - age
        bot.send_message(message.chat.id, f'Ты родился в {birth_year} году, Энекэш')
    except ValueError:
        bot.send_message(message.chat.id, 'эээ, введи число!')
        bot.register_next_step_handler(message,calculate_birth_year )

bot.polling(none_stop=True)

#bot father=7304500465:AAFXdZtysg1HEHo-lvZs__CWmDl2S6JARz8
