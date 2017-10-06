import config

from telegram.ext import Updater
from telegram.ext import CommandHandler

def start_bot(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Добро пожаловать!")

updater = Updater(config.TOKEN)
start_handler = CommandHandler('start', start_bot) #Реакция на команду /start: вывод приветственного сообщения.

updater.dispatcher.add_handler(start_handler) #Создание обработчика.
updater.start_polling() #Запуск бота.


#BOT = telebot.TeleBot(config.TOKEN)

#if __name__ == '__main__':
#    BOT.polling(none_stop=True)
