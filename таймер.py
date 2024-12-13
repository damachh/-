import time
import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['timer'])
def start_timer(message):
    try:
        seconds = int(message.text.split()[1])
        bot.reply_to(message, f"Таймер запущен на {seconds} секунд...")
        time.sleep(seconds)
        bot.reply_to(message, "Время вышло!")
    except (IndexError, ValueError):
        bot.reply_to(message, "Использование: /timer <секунды>")

bot.polling()