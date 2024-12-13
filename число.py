import random
import telebot

bot = telebot.TeleBot('')
secret_number = random.randint(1, 100)
attempts = 0

@bot.message_handler(commands=['start'])
def start_game(message):
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    bot.reply_to(message, "Я загадал число от 1 до 100. Угадай!")

@bot.message_handler(func=lambda message: True)
def guess_number(message):
    global attempts
    try:
        guess = int(message.text)
        attempts += 1
        if guess == secret_number:
            bot.reply_to(message, f"Ура! Ты угадал за {attempts} попыток!")
        elif guess < secret_number:
            bot.reply_to(message, "Больше!")
        else:
            bot.reply_to(message, "Меньше!")
    except ValueError:
        bot.reply_to(message, "Введи число!")

bot.polling()