import random
import telebot

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

choices = ['камень', 'ножницы', 'бумага']


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Хочешь сыграть в игру "Камень, ножницы, бумага"? Напиши свой ход: камень, ножницы или бумага.')

@bot.message_handler(func=lambda message: message.text.lower() in choices)
def play(message):
    user_choice = message.text.lower()
    bot_choice = random.choice(choices)


    if user_choice == bot_choice:
        result = 'Ничья!'
    elif user_choice == 'камень' and bot_choice == 'ножницы':
        result = 'Ты выиграл!'
    elif user_choice == 'ножницы' and bot_choice == 'бумага':
        result = 'Ты выиграл!'
    elif user_choice == 'бумага' and bot_choice == 'камень':
        result = 'Ты выиграл!'
    else:
        result = 'Я выиграл!'

    bot.reply_to(message, f'Ты выбрал {user_choice}, а я выбрал {bot_choice}. {result}')

bot.polling()