import config

from telegram.ext import Updater
from telegram.ext import CommandHandler

def start_bot(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Добро пожаловать!")

    
def launch(token):
    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start_bot) #Реакция на команду /start: вывод приветственного сообщения.

    dispatcher.add_handler(start_handler) #Создание обработчика.
    updater.start_polling() #Запуск бота.


if __name__ == '__main__':
    launch(token=config.TOKEN)
