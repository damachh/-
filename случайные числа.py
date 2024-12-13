import telebot
import random

bot = telebot.TeleBot('')

@bot.message_handler(commands=['random'])
def send_random_number(message):
    num = random.randint(1, 10)
    bot.reply_to(message, f"Случайное число: {num}")

bot.polling()