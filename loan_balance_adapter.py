from chatterbot.logic import LogicAdapter


class MyLogicAdapterLoanBalance(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['account balance', 'balance']
        saving_words = ['loan','loans']
        if any(x in statement.text.lower().split() for x in saving_words):
            return True
        else:
            return False
    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        #import requests
        #import randoms
        # Make a request to the temperature API
        #response = requests.get('https://api.temperature.com/current?units=celsius')
        #data = response.json()

        # Let's base the confidence value on if the request was successful
        
        import pandas as pd
        import numpy as np
        data = pd.read_csv('F:/Chatbot/Chatterbot/Project_v3/Bank_Transactions.csv')
        print(data)
        balance = data[(data['DATE']==max(data['DATE'])) & (data['Account Type']=='Loan')]['BALANCE AMT'].iloc[0]
        print(balance)
        if balance > 0:
            confidence = 1
        else:
            confidence = 0
        print('confidence',confidence)
        response_statement = Statement(text='The current balance in your Loan account is INR {}'.format(balance))
        #response_statement = Statement(text='The current balance in your Loan account is 1000.')
        print('response_statement = ',response_statement)
        #response_statement = input_statement
        response_statement.confidence = confidence
        
        return response_statement

