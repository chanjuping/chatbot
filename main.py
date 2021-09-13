#!/usr/bin/env python

## Import the chatterbot module installed from PIP
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

## Create a bot with logic adapters
## BestMatch chooses from a list of responses
## TimeLogic detects and answers time-based queries

bot = ChatBot(
    'Sparky',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        # 'chatterbot.logic.TimeLogicAdapter'
    ]
)

## Train bot based on list of responses
trainer = ListTrainer(bot)

## List of responses
trainer.train([
    'Hi',
    'Hello',
    'It may be a good idea to join a hackathon',
    'I have a query',
    'Who are you',
    'Who am I',
    'Please elaborate your concern',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
    'You may test that assumption at your convenience'
    'KAI SU TEKNON',
    'Sage art: True several thousand BONKS!',
    'Are you not shocked?',
    'I got a lot going on lately',
    'Looks like you do not have any health insurance so we are gonna let you die',
    'We regret to inform you the Third Impact is in progress',
    'To Fuck Around is Human. To Find Out is Divine.',
    'Every dead body on Everest was once a highly motivated person so... Maybe calm down.',
    'I am going to defeat you with the power of friendship, and this gun I found.',
    'Run. Run as Administrator.',
    'TAKE ONLY PHOTOS. LEAVE ONLY FOOTPRINTS. KILL ONLY TIM.'
])

## Neverending loop 

while True:
    request = input('Say something: ')
    if request == 'bye' or request == 'exit':
        print('Bot: Goodbye')
        break
    else:
        response = bot.get_response(request)
        print('Sparky:', response)