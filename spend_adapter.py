from chatterbot.logic import LogicAdapter

class MySpendAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['month', 'year']
        analyse_words = ['analyse', 'assess','overview']
        period_words = ['current','previous','this','last']
        if any(x in statement.text.lower().split() for x in words) and any(x in statement.text.lower().split() for x in analyse_words) or any(x in statement.text.lower().split() for x in period_words):
            return True
        else:
            return False
    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement        
        import pandas as pd
        mylist=[];
        output='';
        balances='';
        data = pd.read_csv('F:/Chatbot/Chatterbot/Project_v3/Bank_Transactions.csv')
        
        balances = data[(data['Month']=='Jan')]['WITHDRAWAL AMT'].groupby(data['Spend Category']).sum()
        print('input_statement',input_statement)
        print('balances',balances)
        
        if str(input_statement).find('current')!=-1 or str(input_statement).find('this')!=-1:
            balances = data[(data['Month']=='Feb')]['WITHDRAWAL AMT'].groupby(data['Spend Category']).sum()
            
        for index,item in balances.items(): 
            mylist.append(index+':'+str(item)+' | ')
        
        for i in mylist:
            output += i
        #response_statement = Statement(text='The current balance in your Savings account is 1000.')
        if str(input_statement).find('current')!=-1 or str(input_statement).find('this')!=-1:
            response_statement = Statement(text='Your spendings for Feb are {}'.format(output))
        else:
            response_statement = Statement(text='Your spendings for Jan are {}'.format(output))
        print('response_statement = ',response_statement)
        response_statement.confidence = 1
        
        return response_statement
    
    