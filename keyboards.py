from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
MAIN_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Геолокация', callback_data='geo'),
                                 InlineKeyboardButton('Станция метро', callback_data='ml')]
                                ])
GEO_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Назад', callback_data='back_to_main')]])
LINES_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Красная', callback_data='red'),
                                  InlineKeyboardButton('Синяя', callback_data='blue')],
                                 [InlineKeyboardButton('Зеленая', callback_data='green'),
                                  InlineKeyboardButton('Оранжевая', callback_data='orange')],
                                 [InlineKeyboardButton('Фиолетовая', callback_data='violet')],
                                 [InlineKeyboardButton('Назад', callback_data='back_to_main')]
                                 ])
RED_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Девяткино', callback_data='StRed1'),
                                InlineKeyboardButton('Гражданский проспект', callback_data='StRed2')],
                               [InlineKeyboardButton('Академическая', callback_data='StRed3'),
                                InlineKeyboardButton('Политехническая', callback_data='StRed4')],
                               [InlineKeyboardButton('Площадь мужества', callback_data='StRed5'),
                                InlineKeyboardButton('Лесная', callback_data='StRed6')],
                               [InlineKeyboardButton('Выборгская', callback_data='StRed7'),
                                InlineKeyboardButton('Площадь Ленина', callback_data='StRed8')],
                               [InlineKeyboardButton('Чернышевская', callback_data='StRed9'),
                                InlineKeyboardButton('Площадь восстания', callback_data='StRed10')],
                               [InlineKeyboardButton('Владимирская', callback_data='StRed11'),
                                InlineKeyboardButton('Пушкинская', callback_data='StRed12')],
                               [InlineKeyboardButton('Технологический институт', callback_data='StRed13'),
                                InlineKeyboardButton('Балтийская', callback_data='StRed14')],
                               [InlineKeyboardButton('Нарвская', callback_data='StRed15'),
                                InlineKeyboardButton('Кировский завод', callback_data='StRed16')],
                               [InlineKeyboardButton('Автово', callback_data='StRed17'),
                                InlineKeyboardButton('Ленинский проспект', callback_data='StRed18')],
                               [InlineKeyboardButton('Проспект Ветеранов', callback_data='StRed19')],
                               [InlineKeyboardButton('Назад', callback_data='ml')]
                               ])
BLUE_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Парнас', callback_data='StBlue1'),
                                 InlineKeyboardButton('Проспект Просвещения', callback_data='StBlue2')],
                                [InlineKeyboardButton('Озерки', callback_data='StBlue3'),
                                 InlineKeyboardButton('Удельная', callback_data='StBlue4')],
                                [InlineKeyboardButton('Пионерская', callback_data='StBlue5'),
                                 InlineKeyboardButton('Черная речка', callback_data='StBlue6')],
                                [InlineKeyboardButton('Петроградская', callback_data='StBlue7'),
                                 InlineKeyboardButton('Горьковская', callback_data='StBlue8')],
                                [InlineKeyboardButton('Невский проспект', callback_data='StBlue9'),
                                 InlineKeyboardButton('Сенная площадь', callback_data='StBlue10')],
                                [InlineKeyboardButton('Технологический институт', callback_data='StBlue11'),
                                 InlineKeyboardButton('Фрунзенская', callback_data='StBlue12')],
                                [InlineKeyboardButton('Московские ворота', callback_data='StBlue13'),
                                 InlineKeyboardButton('Электросила', callback_data='StBlue14')],
                                [InlineKeyboardButton('Парк Победы', callback_data='StBlue15'),
                                 InlineKeyboardButton('Московская', callback_data='StBlue16')],
                                [InlineKeyboardButton('Звездная', callback_data='StBlue17'),
                                 InlineKeyboardButton('Купчино', callback_data='StBlue18')],
                                [InlineKeyboardButton('Назад', callback_data='ml')]
                                ])
GREEN_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Приморская', callback_data='StGreen1'),
                                  InlineKeyboardButton('Василеостровская', callback_data='StGreen2')],
                                 [InlineKeyboardButton('Гостиный двор', callback_data='StGreen3'),
                                  InlineKeyboardButton('Маяковская', callback_data='StGreen4')],
                                 [InlineKeyboardButton('Площадь А.Невского', callback_data='StGreen5'),
                                  InlineKeyboardButton('Елизаровская', callback_data='StGreen6')],
                                 [InlineKeyboardButton('Ломоносовская', callback_data='StGreen7'),
                                  InlineKeyboardButton('Пролетарская', callback_data='StGreen8')],
                                 [InlineKeyboardButton('Обухово', callback_data='StGreen9'),
                                  InlineKeyboardButton('Рыбацкое', callback_data='StGreen10')],
                                 [InlineKeyboardButton('Назад', callback_data='ml')]
                                 ])
ORANGE_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Спасская', callback_data='StOrange1'),
                                   InlineKeyboardButton('Достоевская', callback_data='StOrange2')],
                                  [InlineKeyboardButton('Лиговский проспект', callback_data='StOrange3'),
				InlineKeyboardButton('Площадь А.Невского', callback_data='StOrange4')],
                                   [InlineKeyboardButton('Новочеркасская', callback_data='StOrange5'),
                                  InlineKeyboardButton('Ладожская', callback_data='StOrange6')],
                                   [InlineKeyboardButton('Проспект Большевиков', callback_data='StOrange7'),
                                  InlineKeyboardButton('Улица Дыбенко', callback_data='StOrange8')],
                                  [InlineKeyboardButton('Назад', callback_data='ml')]
                                  ])
VIOLET_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Комендантский проспект', callback_data='StViolet1'),
                                   InlineKeyboardButton('Старая Деревня', callback_data='StViolet2')],
                                  [InlineKeyboardButton('Крестовский остров', callback_data='StViolet3'),
                                   InlineKeyboardButton('Чкаловская', callback_data='StViolet4')],
                                  [InlineKeyboardButton('Спортивная', callback_data='StViolet5'),
                                   InlineKeyboardButton('Адмиралтейская', callback_data='StViolet6')],
                                  [InlineKeyboardButton('Садовая', callback_data='StViolet7'),
                                   InlineKeyboardButton('Звенигородская', callback_data='StViolet8')],
                                  [InlineKeyboardButton('Обводный канал', callback_data='StViolet9'),
                                   InlineKeyboardButton('Волковская', callback_data='StViolet10')],
                                  [InlineKeyboardButton('Бухарестская', callback_data='StViolet11'),
                                   InlineKeyboardButton('Международная', callback_data='StViolet12')],
                                  [InlineKeyboardButton('Назад', callback_data='ml')]
                                  ])
RADIUS_KB = InlineKeyboardMarkup ([[InlineKeyboardButton('500 метров', callback_data='500'),
                                   InlineKeyboardButton('700 метров', callback_data='700')],
                                   [InlineKeyboardButton('1000 метров', callback_data='1000')],
                                   [InlineKeyboardButton('Назад', callback_data='back_to_main')]
                                   ])

