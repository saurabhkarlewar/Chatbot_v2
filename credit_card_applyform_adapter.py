from chatterbot.logic import LogicAdapter

class MyLogicAdapterAccountBalance(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['account balance', 'balance','accounts','balances','account balances']
        if any(x in statement.text.lower().split() for x in words):
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
        mylist=[];
        output='';
        data = pd.read_csv('F:/Chatbot/Chatterbot/Project_v3/Bank_Transactions.csv')
        balances = data[(data['DATE']==max(data['DATE']))]['BALANCE AMT'].groupby(data['Account Type']).sum()
        for index,item in balances.items(): 
            mylist.append(index+':'+str(item)+' | ')
        
        for i in mylist:
            output += i
        
        confidence = 1
        
        response_statement = Statement(text='Your account balances are {}'.format(output))
        #response_statement = Statement(text='The current balance in your Savings account is 1000.')
        print('response_statement = ',response_statement)
        #response_statement = input_statement
        response_statement.confidence = confidence
        
        return response_statement