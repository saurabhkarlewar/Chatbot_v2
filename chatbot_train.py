from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    bot = ChatBot('BankingBot')
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer = ListTrainer(bot)

    for files in os.listdir('F:/Chatbot/Chatterbot/Project_v2/chatterbot-corpus/english/'):
        data = open('F:/Chatbot/Chatterbot/Project_v2/chatterbot-corpus/english/' + files,'r').readlines()
        trainer.train(data)

setup()