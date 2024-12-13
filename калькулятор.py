import telebot

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, str(result))
    except:
        bot.reply_to(message, 'Пожалуйста, напишите цифры для вычислений.')

bot.polling()