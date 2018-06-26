import telebot
from telebot import types

import config      # contains configuration variables
import algorithms  # contains all the algorithms used in bot


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) # start command handler
def start_bot(message):                  # here I`ll need to ckeck does start command have a refferal llink in it
	user_id = message.chat.id            # message sender ID / referral ID
	link = message.text                  # link which I need to check


	

if __name__ == '__main__':
	bot.polling(none_stop=True)
