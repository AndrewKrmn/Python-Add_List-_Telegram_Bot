import telebot
from telebot import types

token = "6659756402:AAGwYhea35qBozf0nED94U3UVko0BARAyy4"

bot = telebot.TeleBot(token)

global_list = []


@bot.message_handler(commands=["start"])
def starting_chat(message):
    bot.send_message(
        message.chat.id,
        "Привіт це Бот для написання списку\n\t\t  якщо не ясно - \help",
    )
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Переглянути список")
    item2 = types.KeyboardButton("Додати до списку")
    item3 = types.KeyboardButton("Видалити зі списку")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Вибери опцію:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Переглянути список")
def show_list(message):
    if global_list == []:
        bot.send_message(message.chat.id, "Список пустий")
    else:
        bot.send_message(message.chat.id, f"Список : {global_list}")


@bot.message_handler(func=lambda message: message.text == "Додати до списку")
def add_list(message):
    bot.send_message(message.chat.id, "Впиши що хочеш добавити :")
    bot.register_next_step_handler(message, add_letter)


def add_letter(message):
    global_list.append(message.text.lower())
    bot.send_message(message.chat.id, "Добавлено!")


@bot.message_handler(func=lambda message: message.text == "Видалити зі списку")
def delete_letter(message):
    bot.send_message(message.chat.id, f"Що видалити?\n{global_list}")
    bot.register_next_step_handler(message, deleting)


def deleting(message):
    if message.text in global_list:
        global_list.remove(message.text.lower())
        bot.send_message(message.chat.id, "Видалено!")
    else:
        bot.send_message(message.chat.id, "Нема такого слова!")


@bot.message_handler(commands=["help"])
def help_command(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=B3dGi6DnuL8")


bot.infinity_polling()
