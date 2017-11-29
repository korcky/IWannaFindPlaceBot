#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from telegram import Location
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters, MessageHandler, RegexHandler

import config
import keyboards
from find_places import find_places
from stations_geo import SUBWAY_STATIONS

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TEXT = """
*{}.* `{}`
*Rating:* `{}`
*Address:* `{}`
*Opening hours:* `{}`
"""


def place_wrapper(index, place):
    text = TEXT.format(index + 1, place['name'], place['rating'], place['vicinity'], place['is_open'])
    location = Location(float(place['geometry']['location']['lng']), float(place['geometry']['location']['lat']))
    return text, location


def start(bot, update, chat_data):
    chat_data.clear()
    update.message.reply_text('Здравствуйте', reply_markup=keyboards.REMOVE_KB)
#    update.message.reply_text('Выберите тип места:', reply_markup=keyboards.PLACE_KB)
    update.message.reply_text('Выберите способ поиска:', reply_markup=keyboards.TYPE_SEARCH_KB)


#def place_type(bot, update, chat_data):
#    query = update.callback_query
#    chat_data['type'] = query.data

#    bot.edit_message_text(text='Выберите способ поиска:',
#                          reply_markup=keyboards.TYPE_SEARCH_KB,
#                          chat_id=query.message.chat_id,
#                          message_id=query.message.message_id)


def geolocation(bot, update):
    query = update.callback_query
    bot.edit_message_text(text='Выберите радиус:',
                          reply_markup=keyboards.RADIUS_KB,
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


def choose_station(bot, update, chat_data):
    query = update.callback_query
    chat_data['location'] = SUBWAY_STATIONS[query.data]
    bot.edit_message_text(text='Выберите радиус:',
                          reply_markup=keyboards.RADIUS_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def set_radius(bot, update, chat_data):
    query = update.callback_query
    chat_data['radius'] = int(query.data)
    if 'location' not in chat_data:
        bot.send_message(query.message.chat_id, text='Где вы?',
                         reply_markup=keyboards.REQUEST_LOCATION_KB)
    else:
        chat_data['nearest_places'] = find_places(chat_data.pop('location'), chat_data['radius'], 'bar') #chat_data['type'])
        chat_data['index'] = 0
        send_place(bot, update, chat_data, query)


def location_handler(bot, update, chat_data):
    location = update.message.location
    chat_data['nearest_places'] = find_places(location, chat_data['radius'], 'bar') #chat_data['type'])
    chat_data['index'] = 0
    send_place(bot, update, chat_data)


def send_place(bot, update, chat_data, query=None):
    if query:
        chat_id = query.message.chat_id
    else:
        chat_id = update.message.chat_id
    if chat_data['index'] == len(chat_data['nearest_places']):
        bot.send_message(chat_id=chat_id, text='К сожалению, мест больше нет:(', reply_markup=keyboards.START_KB)
    text, location = place_wrapper(chat_data['index'], chat_data['nearest_places'][chat_data['index']])
    bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboards.NEXT_KB, parse_mode='Markdown')
    bot.send_location(chat_id=chat_id, location=location)
    chat_data['index'] += 1
    if chat_data['index'] == len(chat_data['nearest_places']):
        bot.send_message(chat_id=chat_id, text='К сожалению, мест больше нет:(', reply_markup=keyboards.START_KB)


def back_to_main(bot, update):
    query = update.callback_query

    bot.edit_message_text(text='Выберите способ поиска:',
                          reply_markup=keyboards.TYPE_SEARCH_KB,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)


def help(bot, update):
    update.message.reply_text('Выберите способ поиска, и наш бот поможет найти лучшие места для отдыха:)')
    update.message.reply_text('Нажмите /start, чтобы начать')


def error(bot, update, error):
    logging.warning('Update {} caused error {}'.format(update, error))


if __name__ == '__main__':
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start, pass_chat_data=True))
#    dispatcher.add_handler(CallbackQueryHandler(place_type, pattern='[(bar)(restaurant)]', pass_chat_data=True))
    dispatcher.add_handler(CallbackQueryHandler(geolocation, pattern='geo'))
    dispatcher.add_handler(CallbackQueryHandler(metro_lines, pattern='ml'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_main, pattern='back_to_main'))
    dispatcher.add_handler(CallbackQueryHandler(which_station, pattern='[(red)(blue)(green)(orange)(violet)]'))
    dispatcher.add_handler(CallbackQueryHandler(set_radius, pattern='[(500)(700)(1000)]', pass_chat_data=True))
    dispatcher.add_handler(CallbackQueryHandler(choose_station, pattern='St', pass_chat_data=True))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler, pass_chat_data=True))
    dispatcher.add_handler(RegexHandler('^(Показать еще...)$', send_place, pass_chat_data=True))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()
