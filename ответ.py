import telebot

bot = telebot.TeleBot("")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "привет" in text:
        bot.reply_to(message, "Привет и тебе!")
    elif "как дела" in text:
        bot.reply_to(message, "Хорошо, спасибо!")
    elif "пока" in text:
        bot.reply_to(message, "Пока-пока!")
    else:
        bot.reply_to(message, "Я не понимаю...")

bot.polling()