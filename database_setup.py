import telebot
import sqlite3

# connect script to bot with help of token
bot =telebot.TeleBot('6382654428:AAEYIWnStZ1u3kFtw-J1LTjtvYwLmcE_mNw')

name = None

@bot.message_handler(commands=["start"])
def start(message):
    #name of database file
    conn =sqlite3.connect("EyeTea.sql")
    #open connection with database
    cur = conn.cursor()

    # Creates a table users with id, name and pass columns if the table does not exist yet
    cur.execute("CREATE TABLE IF NOT EXISTS users(id int auto_increment primary key, name varchar(50), pass varchar(50))")
    # Synchronisation with database
    conn.commit()
    #Close connection with database
    cur.close()
    #Close connection
    conn.close()

    bot.send_message(message.chat.id, "Hello, now we are going to register you! Please enter your name")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Enter Password")
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect("EyeTea.sql")
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES('%s', '%s')" % (name, password))

    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("List of Users", callback_data="users"))
    bot.send_message(message.chat.id, "User registered",reply_markup=markup)



"""
This function prints info about users
"""
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect("EyeTea.sql")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    info = ""
    for el in users:
        info += f"Name: {el[1]}, Password: {el[2]}\n"
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)


# for non-stop working bot
bot.polling(none_stop=True)
