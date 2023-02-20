import telebot
import random
# from TOKEN import TOKEN
import os, json

# TODO add your Token from telegram
bot = telebot.TeleBot(os.getenv("TOKEN"))
point = 0
use_list = []
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Мои очки')
    itembtn2 = telebot.types.KeyboardButton('Использованые слова')
    keyboard.add(itembtn1, itembtn2 )
    bot.send_message(message.chat.id, "Hello, {0.first_name}. Let's play in the cities of Ukraine.\nYou start first.\n Enter city name to get started!\nFor each correct answer you get 1 point\nYou can view your points by clicking on the 'My points' button".format(message.from_user), reply_markup=keyboard)

with open("ua.json", 'r', encoding='utf-8') as f:
    datas = json.load(f)

data = [item['city'] for item in datas]

@bot.message_handler(content_types=['text'])
def echo_message(message):
    global point
    global use_list 
    if message.text == "Мои очки":
        bot.send_message(message.chat.id,point)
    elif message.text == "Использованые слова":
        for el in use_list:
            bot.send_message(message.chat.id,el)
    else:
        if message.text in data:
            use_list.append(message.text.capitalize())
            data.remove(message.text) 
            # if message.text in use_list:
            #     bot.send_message(message.chat.id, "Вы уже использовали это слово")
            # else:
            for i in data:
                if str(message.text[-1]).capitalize() == str(i[0]).capitalize():
                    bot.send_message(message.chat.id,i)
                    point+=1
                    data.remove(i)
                    break
        
        else:
            bot.send_message(message.chat.id, "Слово не сущестует или неправильно введено!")


bot.infinity_polling()


