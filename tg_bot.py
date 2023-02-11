import telebot
import random
from TOKEN import TOKEN
import os

bot = telebot.TeleBot(os.environ[TOKEN])

# list of cities to choose from 
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 
          'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
# list of already used cities 
used_cities = []


@bot.message_handler(commands=['start'])
def start(message):

    # send welcome message 
    bot.send_message(message.chat.id, "Hi there! Let's play a game! I'll pick a city and you guess which one it is!")

    # pick random city from the list 
    city = random.choice(cities)

    # make sure the city hasn't been used yet 
    while city in used_cities: 
        city = random.choice(cities)

    # add the chosen city to the list of used cities 
    used_cities.append(city)

    # send the chosen city to the user 
    bot.send_message(message.chat.id, "Which city am I thinking of? Hint: It's in the United States.")

     # wait for user's answer 
    bot.register_next_step_handler(message, check_answer, city)

    
def check_answer(message, city): 

    if message == city: 

        # send success message and start again with another random city if answer is correct  
        bot.send_message(message.chat.id, "That's right! Let's try another one!")  

        # pick new random city from list  
        newcity = random.choice(cities)  

        # make sure it hasn't been used yet  
        while newcity in used_cities:  
            newcity = random.choice(cities)  

       # add the chosen newcity to the list of used cities  
        used_cities.append(newcity)  

       # send the chosen newcity to the user  
        bot.send_message(message.chat)