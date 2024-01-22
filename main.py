import telebot
from telebot import types

bot = telebot.TeleBot('6810511847:AAGt_UzwGTKlrWSLcAKkBGn0AguQUKqoEig')

# Словарь для хранения текста пользователя
user_texts = {}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website_pixel = types.KeyboardButton('/pixel-art')
    website_croodles = types.KeyboardButton('/croodles_neutral')
    website_icon = types.KeyboardButton('/icon')
    website_fun = types.KeyboardButton('/fun-emoji')
    website_adve = types.KeyboardButton('/adventurer')
    website_adve2 = types.KeyboardButton('/adventurer-neutral')
    website_lorelei = types.KeyboardButton('/lorelei-neutral')
    website_big = types.KeyboardButton('/big-ears')
    website_botts = types.KeyboardButton('/bottts')
    #start = types.KeyboardButton('/start')

    markup.add(website_pixel, website_croodles, website_icon, website_botts,website_fun,website_adve,website_adve2, website_lorelei, website_big)

    mess = f'Привет, <b><u>{message.from_user.first_name}</u></b> я умею генерировать картинки. Выбери стиль'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['pixel-art'])
def request_text_dicebear(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "pixel")


@bot.message_handler(commands=['croodles_neutral'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "croodles")


@bot.message_handler(commands=['icon'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "icon")


@bot.message_handler(commands=['bottts'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "bottts")

@bot.message_handler(commands=['fun-emoji'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "emoji")

@bot.message_handler(commands=['adventurer'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "advent")

@bot.message_handler(commands=['adventurer-neutral'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "adventneut")


@bot.message_handler(commands=['lorelei-neutral'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "lorelei")


@bot.message_handler(commands=['big-ears'])
def request_text_croodles(message):
    markup = types.ReplyKeyboardRemove()

    # Просим пользователя ввести текст
    msg = bot.send_message(message.chat.id, "Введите имя для генерации картинки", reply_markup=markup)

    # Сохраняем chat_id в словаре для последующего использования
    user_texts[message.chat.id] = (msg.message_id, "big")




@bot.message_handler(func=lambda message: True)
def generate_link(message):
    # Проверяем, есть ли сообщение в словаре
    if message.chat.id in user_texts:
        # Получаем введенный пользователем текст
        user_text = message.text

        # Заменяем пробелы в тексте на подчеркивания
        user_text = user_text.replace(" ", "_")

        # Пример изменения регистра текста
        user_text = user_text.upper()

        # Определяем тип ссылки (dicebear или croodles)
        msg_id, link_type = user_texts[message.chat.id]

        if link_type == "pixel":
            pixel_link = f"https://api.dicebear.com/7.x/pixel-art/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {pixel_link}')
        elif link_type == "icon":
            icon_link = f"https://api.dicebear.com/7.x/icons/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {icon_link}')
        elif link_type == "croodles":
            croodles_link = f"https://api.dicebear.com/7.x/croodles-neutral/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {croodles_link}')
        elif link_type == "bottts":
            bottts_link = f"https://api.dicebear.com/7.x/bottts/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {bottts_link}')
        elif link_type == "emoji":
            emoji_link = f"https://api.dicebear.com/7.x/fun-emoji/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {emoji_link}')
        elif link_type == "advent":
            adve_link = f"https://api.dicebear.com/7.x/adventurer/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {adve_link}')
        elif link_type == "adventneut":
            adveneu_link = f"https://api.dicebear.com/7.x/adventurer-neutral/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {adveneu_link}')
        elif link_type == "lorelei":
            lorel_link = f"https://api.dicebear.com/7.x/lorelei-neutral/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {lorel_link}')
        elif link_type == "big":
            big_link = f"https://api.dicebear.com/7.x/big-ears/svg?seed={user_text}"
            bot.send_message(message.chat.id, f'Ваша ссылка: {big_link}')

        # Удаляем сообщение из словаря
        del user_texts[message.chat.id]

        # Восстанавливаем активные кнопки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        website_pixel = types.KeyboardButton('/pixel-art')
        website_croodles = types.KeyboardButton('/croodles_neutral')
        website_icon = types.KeyboardButton('/icon')
        website_botts = types.KeyboardButton('/bottts')
        website_fun = types.KeyboardButton('/fun-emoji')
        website_adve = types.KeyboardButton('/adventurer')
        website_adve2 = types.KeyboardButton('/adventurer-neutral')
        website_lorelei = types.KeyboardButton('/lorelei-neutral')
        website_big = types.KeyboardButton('/big-ears')

        markup.add(website_pixel, website_croodles, website_icon, website_botts,website_fun,website_adve,website_adve2, website_lorelei, website_big)


        # Отправляем сообщение с восстановленными кнопками
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
