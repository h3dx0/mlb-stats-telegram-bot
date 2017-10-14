from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
import mlbgame
import datetime

updater = Updater(token='466300996:AAEzKqfJO_K16tUVaClDU2QfbaceBbnhjSY')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello I am the bot that will help you to know the MLB results")

def today_stats(bot, update):
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    games = mlbgame.day(year, month, day)
    msg = ""
    for game in games:
        game_txt = "{}\n".format(game)
        msg += game_txt
    bot.send_message(chat_id=update.message.chat_id, text=msg)

start_handler = CommandHandler('start', start)
stats_handler = CommandHandler('today', today_stats)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(stats_handler)

updater.start_polling()
