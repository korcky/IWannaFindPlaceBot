from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

REQUEST_LOCATION_KB = ReplyKeyboardMarkup([[KeyboardButton('Я здесь', request_location=True)]],
                                          resize_keyboard=True)

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

RED_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Девяткино', callback_data='redSt1'),
                                InlineKeyboardButton('Гражданский проспект', callback_data='redSt2')],
                               [InlineKeyboardButton('Академическая', callback_data='redSt3'),
                                InlineKeyboardButton('Политехническая', callback_data='redSt4')],
                               [InlineKeyboardButton('Площадь мужества', callback_data='redSt5'),
                                InlineKeyboardButton('Лесная', callback_data='redSt6')],
                               [InlineKeyboardButton('Выборгская', callback_data='redSt7'),
                                InlineKeyboardButton('Площадь Ленина', callback_data='redSt8')],
                               [InlineKeyboardButton('Чернышевская', callback_data='redSt9'),
                                InlineKeyboardButton('Площадь восстания', callback_data='redSt10')],
                               [InlineKeyboardButton('Владимирская', callback_data='redSt11'),
                                InlineKeyboardButton('Пушкинская', callback_data='redSt12')],
                               [InlineKeyboardButton('Технологический институт', callback_data='redSt13'),
                                InlineKeyboardButton('Балтийская', callback_data='redSt14')],
                               [InlineKeyboardButton('Нарвская', callback_data='redSt15'),
                                InlineKeyboardButton('Кировский завод', callback_data='redSt16')],
                               [InlineKeyboardButton('Автово', callback_data='redSt17'),
                                InlineKeyboardButton('Ленинский проспект', callback_data='redSt18')],
                               [InlineKeyboardButton('Проспект Ветеранов', callback_data='redSt19')],
                               [InlineKeyboardButton('Назад', callback_data='ml')]
                               ])

BLUE_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Парнас', callback_data='blueSt1'),
                                 InlineKeyboardButton('Проспект Просвещения', callback_data='blueSt2')],
                                [InlineKeyboardButton('Озерки', callback_data='blueSt3'),
                                 InlineKeyboardButton('Удельная', callback_data='blueSt4')],
                                [InlineKeyboardButton('Пионерская', callback_data='blueSt5'),
                                 InlineKeyboardButton('Черная речка', callback_data='blueSt6')],
                                [InlineKeyboardButton('Петроградская', callback_data='blueSt7'),
                                 InlineKeyboardButton('Горьковская', callback_data='blueSt8')],
                                [InlineKeyboardButton('Невский проспект', callback_data='blueSt9'),
                                 InlineKeyboardButton('Сенная площадь', callback_data='blueSt10')],
                                [InlineKeyboardButton('Технологический институт', callback_data='blueSt11'),
                                 InlineKeyboardButton('Фрунзенская', callback_data='blueSt12')],
                                [InlineKeyboardButton('Московские ворота', callback_data='blueSt13'),
                                 InlineKeyboardButton('Электросила', callback_data='blueSt14')],
                                [InlineKeyboardButton('Парк Победы', callback_data='blueSt15'),
                                 InlineKeyboardButton('Московская', callback_data='blueSt16')],
                                [InlineKeyboardButton('Звездная', callback_data='blueSt17'),
                                 InlineKeyboardButton('Купчино', callback_data='blueSt18')],
                                [InlineKeyboardButton('Назад', callback_data='ml')]
                                ])

GREEN_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Приморская', callback_data='greenSt1'),
                                  InlineKeyboardButton('Василеостровская', callback_data='greenSt2')],
                                 [InlineKeyboardButton('Гостиный двор', callback_data='greenSt3'),
                                  InlineKeyboardButton('Маяковская', callback_data='greenSt4')],
                                 [InlineKeyboardButton('Площадь А.Невского', callback_data='greenSt5'),
                                  InlineKeyboardButton('Елизаровская', callback_data='greenSt6')],
                                 [InlineKeyboardButton('Ломоносовская', callback_data='greenSt7'),
                                  InlineKeyboardButton('Пролетарская', callback_data='greenSt8')],
                                 [InlineKeyboardButton('Обухово', callback_data='greenSt9'),
                                  InlineKeyboardButton('Рыбацкое', callback_data='greenSt10')],
                                 [InlineKeyboardButton('Назад', callback_data='ml')]
                                 ])

ORANGE_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Спасская', callback_data='orangeSt1'),
                                   InlineKeyboardButton('Достоевская', callback_data='orangeSt2')],
                                  [InlineKeyboardButton('Лиговский проспект', callback_data='orangeSt3'),
                                   InlineKeyboardButton('Новочеркасская', callback_data='orangeSt4')],
                                  [InlineKeyboardButton('Ладожская', callback_data='orangeSt5'),
                                   InlineKeyboardButton('Проспект Большевиков', callback_data='orangeSt6')],
                                  [InlineKeyboardButton('Улица Дыбенко', callback_data='orangeSt7')],
                                  [InlineKeyboardButton('Назад', callback_data='ml')]
                                  ])

VIOLET_KB = InlineKeyboardMarkup([[InlineKeyboardButton('Комендантский проспект', callback_data='violetSt1'),
                                   InlineKeyboardButton('Старая Деревня', callback_data='violetSt2')],
                                  [InlineKeyboardButton('Крестовский остров', callback_data='violetSt3'),
                                   InlineKeyboardButton('Чкаловская', callback_data='violetSt4')],
                                  [InlineKeyboardButton('Спортивная', callback_data='violetSt5'),
                                   InlineKeyboardButton('Адмиралтейская', callback_data='violetSt6')],
                                  [InlineKeyboardButton('Садовая', callback_data='violetSt7'),
                                   InlineKeyboardButton('Звенигородская', callback_data='violetSt8')],
                                  [InlineKeyboardButton('Обводный канал', callback_data='violetSt9'),
                                   InlineKeyboardButton('Волковская', callback_data='violetSt10')],
                                  [InlineKeyboardButton('Бухарестская', callback_data='violetSt11'),
                                   InlineKeyboardButton('Международная', callback_data='violetSt12')],
                                  [InlineKeyboardButton('Назад', callback_data='ml')]
                                  ])

RADIUS_KB = InlineKeyboardMarkup([[InlineKeyboardButton('500 метров', callback_data='500'),
                                   InlineKeyboardButton('700 метров', callback_data='700')],
                                  [InlineKeyboardButton('1000 метров', callback_data='1000')],
                                  [InlineKeyboardButton('Назад', callback_data='back_to_main')]
                                  ])
