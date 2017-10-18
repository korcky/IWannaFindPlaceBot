import config

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

main_kb = InlineKeyboardMarkup([[InlineKeyboardButton('Geolocation', callback_data='geo'),
                                 InlineKeyboardButton('Metro station', callback_data='ms')]])
lines_kb = InlineKeyboardMarkup([[InlineKeyboardButton('Line 1', callback_data='red'),
                                  InlineKeyboardButton('Line 2', callback_data='blue')]])


def start(bot, update):
    update.message.reply_text('Please choose method:', reply_markup=main_kb)


def geolocation(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='There\'s nothing here right now.',
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def metro_station(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Please choose line:',
                          reply_markup=lines_kb,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text('Use /start to use this bot.')


def error(bot, update, error):
    logging.warning('Update {} caused error {}'.format(update, error))


# Create the Updater and pass it your bot's token.
updater = Updater(config.TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(geolocation, pattern='geo'))
updater.dispatcher.add_handler(CallbackQueryHandler(metro_station, pattern='ms'))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
