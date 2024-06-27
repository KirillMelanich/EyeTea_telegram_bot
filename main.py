import telebot
import webbrowser

# connect script to bot with help of token
bot =telebot.TeleBot('6382654428:AAEYIWnStZ1u3kFtw-J1LTjtvYwLmcE_mNw')

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