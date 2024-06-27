import telebot

bot =telebot.TeleBot('6382654428:AAEYIWnStZ1u3kFtw-J1LTjtvYwLmcE_mNw')

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Hello")


bot.polling(none_stop=True)