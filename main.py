import telebot
from telebot import types

import cherrypy

import config      # contains configuration variables
# import algorithms  # contains all the algorithms used in bot


bot = telebot.TeleBot(config.token)


WEBHOOK_HOST = '194.87.101.182'
WEBHOOK_PORT = 443  
WEBHOOK_LISTEN = '194.87.101.182'  

WEBHOOK_SSL_CERT = './YOURPUBLIC.pem'
WEBHOOK_SSL_PRIV = './YOURPRIVATE.key'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)



class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))



@bot.message_handler(commands=['start']) # start command handler
def start_bot(message):                  # here I`ll need to ckeck does start command have a refferal llink in it
	user_id = message.chat.id            # message sender ID / referral ID
	link = message.text                  # link which I need to check
	bot.send_message(user_id, 'a')

	# greatings


cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})


cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
