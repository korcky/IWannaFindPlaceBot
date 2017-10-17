import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Hi!')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in ['Моя геолокация', 'Станция метро']])
    bot.send_message(message.chat.id, 'Выбери способ поиска',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):

    if c.data == 'Моя геолокация':
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Мы работаем над этим;)',
            parse_mode='Markdown'
        )

    elif c.data == 'Станция метро':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                       ['Линия 1', 'Линия 2','Линия 3', 'Линия 4', 'Линия 5']])
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите ветку',
            parse_mode='Markdown',
            reply_markup=keyboard
        )
    else:
        keyboard = types.InlineKeyboardMarkup()
        if c.data == 'Линия 1':
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                           ['Девяткино', 'Гражданский проспект', 'Академическая', 'Политехническая', 'Площадь Мужества',
                            'Лесная', 'Выборгская', 'Площадь Ленина', 'Чернышевская', 'Площадь Восстания',
                            'Владимирская', 'Пушкинская', 'Технологический институт', 'Балтийская', 'Нарвская',
                            'Кировский завод', 'Автово', 'Ленинский просппект', 'Проспект Ветеранов']])
        elif c.data == 'Линия 2':
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                           ['Парнас', 'Проспект Просвещения', 'Озерки', 'Удельная', 'Пионерская',
                            'Черная речка', 'Петроградская', 'Горьковская', 'Невский проспект',
                            'Сенная площадь', 'Технологический институт', 'Фрунзенская',
                            'Московские ворота', 'Электросила', 'Парк Победы', 'Московская',
                            'Звездная', 'Купчино']])
        elif c.data == 'Линия 3':
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                           ['Приморская', 'Василеостровская', 'Гостиный двор', 'Маяковская',
                            'Площадь А.Невского', 'Елизаровская', 'Ломоносовская', 'Пролетарская',
                            'Обухово', 'Рыбацкое']])
        elif c.data == 'Линия 4':
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                           ['Спасская', 'Достоевская', 'Лиговский проспект', 'Новочеркасская',
                            'Ладожская', 'Проспект Большевиков', 'Улица Дыбенко']])
        elif c.data == 'Линия 5':
            keyboard.add(*[types.InlineKeyboardButton(text=name, callback_data=name) for name in
                           ['Комендантский проспект', 'Старая Деревня', 'Крестовский остров',
                            'Чкаловская', 'Спортивная', 'Адмиралтейская', 'Садовая', 'Звенигородская',
                            'Обводный канал', 'Волковская', 'Бухарестская', 'Международная']])

        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Выберите станцию',
            parse_mode='Markdown',
            reply_markup=keyboard
        )


if __name__ == '__main__':
    bot.polling(none_stop=True)
