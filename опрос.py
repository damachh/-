import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['poll'])
def create_poll(message):
    question = "Какой ваш любимый язык программирования?"
    options = ["Python", "JavaScript", "C++", "Java"]
    keyboard = telebot.types.InlineKeyboardMarkup()
    for option in options:
        button = telebot.types.InlineKeyboardButton(option, callback_data=option)
        keyboard.add(button)
    bot.send_message(message.chat.id, question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_poll_answer(call):
    bot.answer_callback_query(call.id, f"Вы выбрали: {call.data}")

bot.polling()