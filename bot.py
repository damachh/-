import telebot
from Tools.scripts.make_ctype import values
from currency_converter import*
from telebot import*
from telebot.types import InlineKeyboardButton

bot = telebot.TeleBot('7304500465:AAFXdZtysg1HEHo-lvZs__CWmDl2S6JARz8')
currency= CurrencyConverter()
amount=0



@bot.message_handler(commands=['start'])
def start(message):

    markup=types.InlineKeyboardMarkup()
    btn1=(types.InlineKeyboardButton('Перейти на Taobao', url='https://www.taobao.com'))
    btn2=(types.InlineKeyboardButton('Перейти на 1688', url='http://1688.com'))
    markup.row(btn1,btn2)
    btn3=(types.InlineKeyboardButton('Перейти на Pinduoduo', url='http://pinduoduo.com'))
    btn4=(types.InlineKeyboardButton('Перейти на Poizon', url='https://www.poizon.com'))
    markup.row(btn3, btn4)
    bot.send_message(message.chat.id,
                     'Привет, дорогой покупатель! Выбери маркетплейс из котрого хочешь сделать заказ. После того как выбрал товар, можешь посмотреть его сумму в других валютах и отправить на него ссылку на тг: @Fairygoodmother11.',reply_markup=markup)


    markup = types.ReplyKeyboardMarkup()
    bn1 = InlineKeyboardButton('Конвертизация Валют')
    bn3 = InlineKeyboardButton('Обратная связь')
    markup.row(bn1, bn3)
    bot.send_message(message.chat.id, ':)', reply_markup=markup)
@bot.message_handler(commands=['money'])
def Y(message):
    bot.send_message(message.chat.id, 'Посмотрим сколько стоит твой товар. Введи сумму')
    bot.register_next_step_handler(message,summa)
def summa(message):
    global amount
    try:
     amount=int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Введите число, пожалуйста!')
        bot.register_next_step_handler(message, summa)
        return
    if amount>0:


        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1= types.InlineKeyboardButton('ЮАНЬ/ЕВРО', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('ДОЛЛАР/ЮАНЬ', callback_data='usd/cny')
        btn3 = types.InlineKeyboardButton('ЮАНЬ/ДОЛЛАР', callback_data='cny/eur')
        btn4 = types.InlineKeyboardButton('ДОЛЛАР/ЕВРО', callback_data='cny/usd')
        markup.row(btn1, btn2)
        markup.row( btn3,btn4)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Хэй, число должно быть положительным')
        bot.register_next_step_handler(message, summa)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    values=call.data.upper().split('/')
    res=currency.convert(amount,values[0],values[1])
    bot.send_message(call.message.chat.id, f'Получается: {res}.')
@bot.message_handler(commands=['accounts'])
def a(message):
    bot.send_message(message.chat.id, 'Для обратной связи: Создатель бота - @abdrwq, Владелец бота:@Fairygoodmother11')
    bot.register_next_step_handler(message, click)

@bot.message_handler()
def click(message):
    if message.text == 'Конвертизация Валют':
        bot.send_message(message.chat.id, "Нажмите /money")
    elif message.text == 'Обратная связь':
        bot.send_message(message.chat.id, 'Нажмите /accounts')
bot.polling(none_stop=True)





