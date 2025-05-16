from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Составить тест"), KeyboardButton(text="Пройти тест")],
        [KeyboardButton(text="Моя статистика"), KeyboardButton(text="Сбросить мой тест")]
    ],
    resize_keyboard=True
)

def get_survey_keyboard(q_num: int) -> InlineKeyboardMarkup:
    """Возвращает клавиатуру для указанного вопроса опроса"""
    if q_num == 1:  # Цвета
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Красный ❤️", callback_data="survey_1_color_red"),
                InlineKeyboardButton(text="Синий 💙", callback_data="survey_1_color_blue")
            ],
            [
                InlineKeyboardButton(text="Зелёный 💚", callback_data="survey_1_color_green"),
                InlineKeyboardButton(text="Чёрный 🖤", callback_data="survey_1_color_black")
            ],
            [
                InlineKeyboardButton(text="Розовый 💗", callback_data="survey_1_color_pink"),
                InlineKeyboardButton(text="Жёлтый 💛", callback_data="survey_1_color_yellow")
            ]
        ])

    elif q_num == 2:  # Еда
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Пицца 🍕", callback_data="survey_2_food_pizza"),
                InlineKeyboardButton(text="Суши 🍣", callback_data="survey_2_food_sushi")
            ],
            [
                InlineKeyboardButton(text="Бургеры 🍔", callback_data="survey_2_food_burger"),
                InlineKeyboardButton(text="Паста 🍝", callback_data="survey_2_food_pasta")
            ],
            [
                InlineKeyboardButton(text="Шашлык 🍖", callback_data="survey_2_food_barbecue"),
                InlineKeyboardButton(text="Салат 🥗", callback_data="survey_2_food_salad")  # Исправлено: "салат"
            ]
        ])

    elif q_num == 3:  # Фильмы/сериалы
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Наруто 🍥", callback_data="survey_3_film_naruto"),
                InlineKeyboardButton(text="Игра престолов 👑", callback_data="survey_3_film_igraprestolov")  # Упрощено
            ],
            [
                InlineKeyboardButton(text="Друзья ☕", callback_data="survey_3_film_friends"),
                InlineKeyboardButton(text="Мстители 🛡️", callback_data="survey_3_film_mstiteli")  # Упрощено
            ],
            [
                InlineKeyboardButton(text="Гарри Поттер ⚡", callback_data="survey_3_film_harrypotter"),  # Упрощено
                InlineKeyboardButton(text="Офис 🏢", callback_data="survey_3_film_ofis")  # Упрощено
            ]
        ])

    elif q_num == 4:  # Музыка
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Поп 🎤", callback_data="survey_4_music_pop"),
                InlineKeyboardButton(text="Рок 🤘", callback_data="survey_4_music_rock")
            ],
            [
                InlineKeyboardButton(text="Хип-хоп 🎧", callback_data="survey_4_music_hiphop"),  # Упрощено
                InlineKeyboardButton(text="Классика 🎻", callback_data="survey_4_music_classic")
            ],
            [
                InlineKeyboardButton(text="Электроника 🎹", callback_data="survey_4_music_electronics"),
                InlineKeyboardButton(text="Шансон 🎶", callback_data="survey_4_music_chanson")
            ]
        ])

    elif q_num == 5:  # Время года
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Лето ☀️", callback_data="survey_5_yeartime_summer"),
                InlineKeyboardButton(text="Зима ❄️", callback_data="survey_5_yeartime_winter")
            ],
            [
                InlineKeyboardButton(text="Весна 🌸", callback_data="survey_5_yeartime_spring"),
                InlineKeyboardButton(text="Осень 🍂", callback_data="survey_5_yeartime_autumn")
            ]
        ])

    elif q_num == 6:  # Напитки
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Кофе ☕", callback_data="survey_6_drink_coffee"),
                InlineKeyboardButton(text="Чай 🫖", callback_data="survey_6_drink_tea")
            ],
            [
                InlineKeyboardButton(text="Сок 🧃", callback_data="survey_6_drink_juice"),
                InlineKeyboardButton(text="Газировка 🥤", callback_data="survey_6_drink_soda")
            ],
            [
                InlineKeyboardButton(text="Вода 💧", callback_data="survey_6_drink_water"),
                InlineKeyboardButton(text="Алкоголь 🍷", callback_data="survey_6_drink_alcohol")
            ]
        ])

    elif q_num == 7:  # Отдых
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Путешествия ✈️", callback_data="survey_7_rest_travel"),
                InlineKeyboardButton(text="Кино 🎬", callback_data="survey_7_rest_cinema")
            ],
            [
                InlineKeyboardButton(text="Спорт ⚽", callback_data="survey_7_rest_sport"),
                InlineKeyboardButton(text="Вечеринки 🎉", callback_data="survey_7_rest_parties")
            ],
            [
                InlineKeyboardButton(text="Домашний уют 🏠", callback_data="survey_7_rest_home"),
                InlineKeyboardButton(text="Прогулки на природе 🌳", callback_data="survey_7_rest_nature")
            ]
        ])

    elif q_num == 8:  # Животные
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Собака 🐶", callback_data="survey_8_animal_dog"),
                InlineKeyboardButton(text="Кошка 🐱", callback_data="survey_8_animal_cat")
            ],
            [
                InlineKeyboardButton(text="Птица 🐦", callback_data="survey_8_animal_bird"),
                InlineKeyboardButton(text="Рыбка 🐠", callback_data="survey_8_animal_fish")
            ],
            [
                InlineKeyboardButton(text="Хомяк 🐹", callback_data="survey_8_animal_hamster"),
                InlineKeyboardButton(text="Никакое 🚫", callback_data="survey_8_animal_none")
            ]
        ])

    elif q_num == 9:  # Праздники
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Новый год 🎄", callback_data="survey_9_holiday_newyear"),
                InlineKeyboardButton(text="День рождения 🎂", callback_data="survey_9_holiday_birthday")
            ],
            [
                InlineKeyboardButton(text="Хэллоуин 🎃", callback_data="survey_9_holiday_halloween"),
                InlineKeyboardButton(text="8 марта / 23 февраля 🌸", callback_data="survey_9_holiday_march8feb23")
            ],
            [
                InlineKeyboardButton(text="Рождество 🎅", callback_data="survey_9_holiday_christmas"),
                InlineKeyboardButton(text="Никакой 🚫", callback_data="survey_9_holiday_none")
            ]
        ])

    elif q_num == 10:  # Спорт
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Футбол ⚽", callback_data="survey_10_sport_football"),
                InlineKeyboardButton(text="Баскетбол 🏀", callback_data="survey_10_sport_basketball")
            ],
            [
                InlineKeyboardButton(text="Теннис 🎾", callback_data="survey_10_sport_tennis"),
                InlineKeyboardButton(text="Плавание 🏊", callback_data="survey_10_sport_swimming")
            ],
            [
                InlineKeyboardButton(text="Бег 🏃", callback_data="survey_10_sport_running"),
                InlineKeyboardButton(text="Никакой 🚫", callback_data="survey_10_sport_none")
            ]
        ])

    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Ошибка", callback_data="error")]])

inline_k_1_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Красный ❤️", callback_data="1_color_red"),
            InlineKeyboardButton(text="Синий 💙", callback_data="1_color_blue")
        ],
        [
            InlineKeyboardButton(text="Зелёный 💚", callback_data="1_color_green"),
            InlineKeyboardButton(text="Чёрный 🖤", callback_data="1_color_black")
        ],
        [
            InlineKeyboardButton(text="Розовый 💗", callback_data="1_color_pink"),
            InlineKeyboardButton(text="Жёлтый 💛", callback_data="1_color_yellow")
        ],
    ]
)

inline_k_2_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пицца 🍕", callback_data="2_food_pizza"),
            InlineKeyboardButton(text="Суши 🍣", callback_data="2_food_sushi")
        ],
        [
            InlineKeyboardButton(text="Бургеры 🍔", callback_data="2_food_burger"),
            InlineKeyboardButton(text="Паста 🍝", callback_data="2_food_pasta")
        ],
        [
            InlineKeyboardButton(text="Шашлык 🍖", callback_data="2_food_barbecue"),
            InlineKeyboardButton(text="Салат 🥗", callback_data="2_food_salad")
        ],
    ]
)

inline_k_3_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наруто 🍥", callback_data="3_film_naruto"),
            InlineKeyboardButton(text="Игра престолов 👑", callback_data="3_film_igraprestolov")
        ],
        [
            InlineKeyboardButton(text="Друзья ☕", callback_data="3_film_friends"),
            InlineKeyboardButton(text="Мстители 🛡️", callback_data="3_film_mstiteli")
        ],
        [
            InlineKeyboardButton(text="Гарри Поттер ⚡", callback_data="3_film_harrypotter"),
            InlineKeyboardButton(text="Офис 🏢", callback_data="3_film_ofis")
        ],
    ]
)

inline_k_4_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Поп 🎤", callback_data="4_music_pop"),
            InlineKeyboardButton(text="Рок 🤘", callback_data="4_music_rock")
        ],
        [
            InlineKeyboardButton(text="Хип-хоп 🎧", callback_data="4_music_hiphop"),
            InlineKeyboardButton(text="Классика 🎻", callback_data="4_music_classic")
        ],
        [
            InlineKeyboardButton(text="Электроника 🎹", callback_data="4_music_electronics"),
            InlineKeyboardButton(text="Шансон 🎶", callback_data="4_music_chanson")
        ],
    ]
)

inline_k_5_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Лето ☀️", callback_data="5_yeartime_summer"),
            InlineKeyboardButton(text="Зима ❄️", callback_data="5_yeartime_winter")
        ],
        [
            InlineKeyboardButton(text="Весна 🌸", callback_data="5_yeartime_spring"),
            InlineKeyboardButton(text="Осень 🍂", callback_data="5_yeartime_autumn")
        ],
    ]
)

inline_k_6_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Кофе ☕", callback_data="6_drink_coffee"),
            InlineKeyboardButton(text="Чай 🫖", callback_data="6_drink_tea")
        ],
        [
            InlineKeyboardButton(text="Сок 🧃", callback_data="6_drink_juice"),
            InlineKeyboardButton(text="Газировка 🥤", callback_data="6_drink_soda")
        ],
        [
            InlineKeyboardButton(text="Вода 💧", callback_data="6_drink_water"),
            InlineKeyboardButton(text="Алкоголь 🍷", callback_data="6_drink_alcohol")
        ],
    ]
)

inline_k_7_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Путешествия ✈️", callback_data="7_rest_travel"),
            InlineKeyboardButton(text="Кино 🎬", callback_data="7_rest_cinema")
        ],
        [
            InlineKeyboardButton(text="Спорт ⚽", callback_data="7_rest_sport"),
            InlineKeyboardButton(text="Вечеринки 🎉", callback_data="7_rest_parties")
        ],
        [
            InlineKeyboardButton(text="Домашний уют 🏠", callback_data="7_rest_home"),
            InlineKeyboardButton(text="Прогулки на природе 🌳", callback_data="7_rest_nature")
        ],
    ]
)

inline_k_8_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Собака 🐶", callback_data="8_animal_dog"),
            InlineKeyboardButton(text="Кошка 🐱", callback_data="8_animal_cat")
        ],
        [
            InlineKeyboardButton(text="Птица 🐦", callback_data="8_animal_bird"),
            InlineKeyboardButton(text="Рыбка 🐠", callback_data="8_animal_fish")
        ],
        [
            InlineKeyboardButton(text="Хомяк 🐹", callback_data="8_animal_hamster"),
            InlineKeyboardButton(text="Никакое 🚫", callback_data="8_animal_none")
        ],
    ]
)

inline_k_9_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Новый год 🎄", callback_data="9_holiday_newyear"),
            InlineKeyboardButton(text="День рождения 🎂", callback_data="9_holiday_birthday")
        ],
        [
            InlineKeyboardButton(text="Хэллоуин 🎃", callback_data="9_holiday_halloween"),
            InlineKeyboardButton(text="8 марта / 23 февраля 🌸", callback_data="9_holiday_march8feb23")
        ],
        [
            InlineKeyboardButton(text="Рождество 🎅", callback_data="9_holiday_christmas"),
            InlineKeyboardButton(text="Никакой 🚫", callback_data="9_holiday_none")
        ],
    ]
)

inline_k_10_question = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Футбол ⚽", callback_data="10_sport_football"),
            InlineKeyboardButton(text="Баскетбол 🏀", callback_data="10_sport_basketball")
        ],
        [
            InlineKeyboardButton(text="Теннис 🎾", callback_data="10_sport_tennis"),
            InlineKeyboardButton(text="Плавание 🏊", callback_data="10_sport_swimming")
        ],
        [
            InlineKeyboardButton(text="Бег 🏃", callback_data="10_sport_running"),
            InlineKeyboardButton(text="Никакой 🚫", callback_data="10_sport_none")
        ],
    ]
)
