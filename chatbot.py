from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging



def get_response(usrText):
    logging.basicConfig(level=logging.INFO)
    bot = ChatBot('BankingBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'banking_service_adapter.MyLogicAdapter'
        },
        {
            'import_path': 'account_balance_adapter.MyLogicAdapterAccountBalance'
        },
        {
            'import_path': 'loan_balance_adapter.MyLogicAdapterLoanBalance'
        },
        {
            'import_path': 'spend_adapter.MySpendAdapter'
        },
        {
            'import_path': 'greetings_adapter.MyGreetingsAdapter'
        },
        {
            'import_path': 'credit_card_apply_adapter.MyCCApplicationAdapter'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'i want to apply for a new credit card',
            'output_text': 'Choose between Basic, Advance or Premier Card. For more details on features click here https://www.google.com/'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'apply for a new credit card',
            'output_text': 'Choose between Basic, Advance or Premier Card. For more details on features click here https://www.google.com/'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.70
        }
    ])
    trainer = ListTrainer(bot)
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break