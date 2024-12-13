import telebot

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

game_map = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def print_map():
    return '\n'.join([' | '.join(row) for row in game_map])

def check_winner(player):
    for i in range(3):
        if all([game_map[i][j] == player for j in range(3)]) or all([game_map[j][i] == player for j in range(3)]):
            return True
    if all([game_map[i][i] == player for i in range(3)]) or all([game_map[i][2-i] == player for i in range(3)]):
        return True
    return False

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, print_map())

@bot.message_handler(func=lambda message: True)
def handle_move(message):
    global current_player

    x, y = map(int, message.text.split())
    if game_map[x][y] == ' ':
        game_map[x][y] = current_player
        if check_winner(current_player):
            bot.send_message(message.chat.id, f'Player {current_player} wins!\n{print_map()}')
            return
        current_player = 'X' if current_player == 'O' else 'O'
    else:
        bot.send_message(message.chat.id, 'Invalid move. Try again.')
        return

    bot.send_message(message.chat.id, print_map())

bot.polling()