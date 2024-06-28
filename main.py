import telebot
from telebot import types
import webbrowser

# connect script to bot with help of token
bot =telebot.TeleBot('6382654428:AAEYIWnStZ1u3kFtw-J1LTjtvYwLmcE_mNw')

def on_click(message):
    if message.text == "Go to the site":
        bot.send_message(message.chat.id, "Website is open")
    elif message.text == "Delete photo":
        bot.send_message(message.chat.id, "Deleted, sucker!")

@bot.message_handler(commands=["start"])
def start(message):
    #creation of the buttons
    markup = types.ReplyKeyboardMarkup()
    btn1 =  types.KeyboardButton("Go to the site")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Delete photo")
    btn3 = types.KeyboardButton("Edit text")
    markup.row(btn2, btn3)
    file = open('./photo.JPEG', "rb")
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, "Hello, motherfucker!", reply_markup=markup)

    bot.register_next_step_handler(message, on_click)


"""
Sends reply's for different files downloads
"""
@bot.message_handler(content_types=["photo", 'audio'])
def get_photo(message):
    #creation of the buttons
    markup = types.InlineKeyboardMarkup()
    btn1 =  types.InlineKeyboardButton("Go to the site", url="https://youtube.com")
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton("Delete photo", callback_data="delete")
    btn3 = types.InlineKeyboardButton("Edit text", callback_data="edit")
    markup.row(btn2, btn3)

    bot.reply_to(message, "What a beautiful photo!", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == "edit":
        bot.edit_message_text("Edit text",callback.message.chat.id, callback.message.message_id)


"""
For sending user to website 
"""
@bot.message_handler(commands=["site", "website"])
def site(message):
    webbrowser.open("https://youtube.com")


"""
This function sends messages after certain commands that starts with "/"
"""
@bot.message_handler(commands=["start", "main", "hello"])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name} {message.from_user.last_name} ")


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, "help yourself motherfucker!")

"""
This function sends messages after anu kind of messages
Important! it must be bellow functions fo commands!!!
"""
@bot.message_handler()
def info(message):
    if message.text.lower() == "hello":
        # for answering as message
        bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name} {message.from_user.last_name} ")
    elif message.text.lower() == "id":
        # for answering as reply
        bot.reply_to(message, f"ID: {message.from_user.id}")


# for non-stop working bot
bot.polling(none_stop=True)

#alternative way for the same purposes
# bot.infinity_polling()