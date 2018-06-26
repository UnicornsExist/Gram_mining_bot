# This script contains all algorithms I use in bot
import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.main_db

users_coll = db.users_coll


def insert_user(message):     # Добавляет юзера в БД
	username = message.chat.username
	user_id = message.chat.id
	balance = 0

	if len(message.text.split()) == 2: # Проверяет, перешёл ли юзер по реферральной ссылке
		referer = message.text.split()[1]
	else:
		referer = ""

	users_coll.insert({'username':username,
		               'telegram_id':user_id,
		               'balance':balance,
		               'referer': referer})
	

def start(message):        # Проверяет, еcть ли юзер в БД
	user_id = message.chat.id
	if users_coll.find_one({'telegram_id':user_id}) == None:
		insert_user(message)  # Добавляем юзера в БД
