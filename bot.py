import logging
import keyboards
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)



def start(bot, update):
    update.message.reply_text('Выберите способ поиска:', reply_markup=keyboards.MAIN_KB)


def geolocation(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Мы работаем над этим',
                          reply_markup=keyboards.GEO_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def metro_lines(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Выберите линию:',
                          reply_markup=keyboards.LINES_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def which_station(bot, update):
    query = update.callback_query
    if query.data == 'red':
        bot.edit_message_text(text='Выберите станцию:',
                              reply_markup=keyboards.RED_KB,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == 'blue':
        bot.edit_message_text(text='Выберите станцию:',
                              reply_markup=keyboards.BLUE_KB,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == 'green':
        bot.edit_message_text(text='Выберите станцию:',
                              reply_markup=keyboards.GREEN_KB,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == 'orange':
        bot.edit_message_text(text='Выберите станцию:',
                              reply_markup=keyboards.ORANGE_KB,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == 'violet':
        bot.edit_message_text(text='Выберите станцию:',
                              reply_markup=keyboards.VIOLET_KB,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)


def back_to_main(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Выбери способ поиска:',
                          reply_markup=keyboards.MAIN_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text('Выберите способ поиска, и наш бот поможет найти лучшие места для отдыха:)')
    update.message.reply_text('Нажмите /start, чтобы начать')

def error(bot, update, error):
    logging.warning('Update {} caused error {}'.format(update, error))


if __name__ == '__main__':
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(geolocation, pattern='geo'))
    dispatcher.add_handler(CallbackQueryHandler(metro_lines, pattern='ml'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_main, pattern='back_to_main'))
    dispatcher.add_handler(CallbackQueryHandler(which_station, pattern='[(red)(blue)(green)(orange)(violet)]'))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
