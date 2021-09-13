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
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

## Train bot based on list of responses
trainer = ListTrainer(bot)

## List of responses
trainer.train([
    'Hi',
    'Hello',
    'I need roadmap for Competitive Programming',
    'Just create an account on GFG and start',
    'I have a query.',
    'Please elaborate, your concern',
    'How long it will take to become expert in Coding ?',
    'It usually depends on the amount of practice.',
    'Ok Thanks',
    'No Problem! Have a Good Day!'
])

## Neverending loop 

while True:
    request=input('Say something: ')
    if request == 'bye' or request == 'exit':
        print('Bot: Goodbye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:', response)