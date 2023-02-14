import telebot
import random
from TOKEN import TOKEN
import os, json, requests

# TODO add your Token from telegram
bot = telebot.TeleBot(TOKEN)
point = 0
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = telebot.types.KeyboardButton('Ваши очки')
    keyboard.add(itembtn1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}\nИграем в игру города Украины.\nДля старта введите название города.".format(message.from_user), reply_markup=keyboard)

with open("koatuu.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

@bot.message_handler(content_types=['text'])
def echo_message(message):
    global point
    if message.text == "Ваши очки":
        bot.send_message(message.chat.id,point)
    else:
        if message.text in data:
            use_list = []
            use_list.append(message.text) 
            data.remove(message.text) 
            if message.text in use_list:
                bot.send_message(message.chat.id, "Вы уже использовали это слово")
            for i in data:
                if str(message.text[-1]).upper() == str(i[0]).upper():
                    bot.send_message(message.chat.id,i)
                    point+=1
                    data.remove(i)
                    break
        
        else:
            bot.send_message(message.chat.id, "Слово не сущестует или неправильно введено!")


bot.infinity_polling()



# import telebot
# import os

# bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

# # list of cities to choose from 
# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 
#           'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
# # list of already used cities 
# used_cities = []


# @bot.message_handler(commands=['start'])
# def start(message):

#     # send welcome message 
#     bot.send_message(message.chat.id, "Hi there! Let's play a game! I'll pick a city and you guess which one it is!")

#     # pick random city from the list 
#     city = random.choice(cities)

#     # make sure the city hasn't been used yet 
#     while city in used_cities: 
#         city = random.choice(cities)

#     # add the chosen city to the list of used cities 
#     used_cities.append(city)

#     # send the chosen city to the user 
#     bot.send_message(message.chat.id, "Which city am I thinking of? Hint: It's in the United States.")

#      # wait for user's answer 
#     bot.register_next_step_handler(message, check_answer, city)

    
# def check_answer(message, city): 

#     if message == city: 

#         # send success message and start again with another random city if answer is correct  
#         bot.send_message(message.chat.id, "That's right! Let's try another one!")  

#         # pick new random city from list  
#         newcity = random.choice(cities)  

#         # make sure it hasn't been used yet  
#         while newcity in used_cities:  
#             newcity = random.choice(cities)  

#        # add the chosen newcity to the list of used cities  
#         used_cities.append(newcity)  

#        # send the chosen newcity to the user  
#         bot.send_message(message.chat)