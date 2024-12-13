import random
import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

facts = [
    "На Земле больше деревьев, чем звезд в Млечном Пути.",
    "Самое длинное слово в английском языке - pneumonoultramicroscopicsilicovolcanoconiosis.",
    "Кролики могут видеть за собой, не поворачивая головы.",
    "Пчелы могут узнавать лица.",
    "В мире больше пластиковых фламинго, чем настоящих.",
    "Сердце человека бьется около 100 000 раз в день.",
    # Добавьте свои факты сюда
]

@bot.message_handler(commands=['start'])
def first(message):
    bot.reply_to(message, "Привет! Я бот-фактов. Напиши /факт, чтобы узнать случайный интересный факт.")

@bot.message_handler(commands=['факт'])
def send_fact(message):
    random_fact = random.choice(facts)
    bot.reply_to(message, random_fact)

bot.polling(none_stop=True)