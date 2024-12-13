import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('7630771581:AAFwCdxFFE56VJjYdfZIl2GThmBalQ2ZnZU')
name = ''


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('d.snd')  # any extension
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()


    bot.send_message(message.chat.id, 'Вас приветствуют бот магазина одежды (имя магазина)!При помощи этого бота вы сможете написать отзыв о нашей одежде,a так же посмотреть отзывы других людей.Напишите любое слово,чтобы посмотреть отзывы других людей,если ничего не вывело,значит отзывов еще нет.После этого напишите /r,чтобы самому написать отзыв.')
    bot.register_next_step_handler(message, get_bd)

def get_bd(message):
    conn = sqlite3.connect('d.snd')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'ТОВАР: {el[1]}, ОТЗЫВ: {el[2]}\n'

    cur.close()
    conn.close()
    bot.send_message(message.chat.id, info)
@bot.message_handler(commands=['r'])
def start(message):
    conn = sqlite3.connect('d.snd') #any extension
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()

    bot.send_message(message.chat.id, 'Для того,чтобы написать отзыв,в первую очередь нужно написать какой товар вы купили.')
    bot.register_next_step_handler(message, get_user_name)

def get_user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Вот теперь можете писать отзыв об этом товаре.')
    bot.register_next_step_handler(message, get_user_pass)

def get_user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('d.snd')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Отзыв добавлен,спасибо за обратную связь.')
bot.polling(none_stop=True)