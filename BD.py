import telebot
import sqlite3

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot = telebot.TeleBot('7767638859:AAEXDLML0totjXDSmscZvLFWNexioDGsWlY')
name = ''

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('db.snd') #any extension
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()

    bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, get_user_name)

def get_user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль:')
    bot.register_next_step_handler(message, get_user_pass)

def get_user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('db.snd')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!')

    conn = sqlite3.connect('db.snd')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(message.chat.id, info)

bot.polling(none_stop=True)