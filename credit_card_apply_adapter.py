from chatterbot.logic import LogicAdapter

class MyCCApplicationAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['apply', 'get']
        product_words = ['credit', 'advance','basic','premier']
        card_words = ['card']
        if any(x in statement.text.lower().split() for x in words) or any(x in statement.text.lower().split() for x in product_words) or any(x in statement.text.lower().split() for x in card_words):
            return True
        else:
            return False
    def process(self, input_statement, additional_response_selection_parameters):
        
        from chatterbot.conversation import Statement     
        import pandas as pd
        import numpy as np
        from datetime import date
        mylist=[];
        output='';
        prdtype='';
        data = pd.read_csv('F:/Chatbot/Chatterbot/Project_v3/ApplicationForm.csv')
        
        if str(input_statement).find('basic')!=-1:
            prdtype='basic'
        elif str(input_statement).find('advance')!=-1:
            prdtype='advance'
        elif str(input_statement).find('premier')!=-1:
            prdtype='premier'
        else:
            prdtype=''
        
        print('prdtype ',prdtype)
        formentry = data.loc[data['Account No']==409000493201]
        
        if prdtype != '':
            print('prdtype not blank ',prdtype)
            if formentry.size > 0:
                print('formentry size ',formentry.size)
                #if formentry['Product Type'] == prdtype:
                output = 'You existing application is in process. Please appy for a new product once you receive the already applied credit card.'
            else:
                data = data.append({'Account No':'409000493201','Name':'Saurabh Karlewar','Application Date':date.today(),'Product':'Card','Product Type':prdtype,'TrackingID':'1234'},ignore_index=True)
                data.to_csv('F:/Chatbot/Chatterbot/Project_v3/ApplicationForm.csv',encoding='utf-8', index=False) 
                output = 'Yor application is successful. Traking ID is 1245'
        else:
            print('prdtype blank ',prdtype)
            output = 'Choose between Basic, Advance or Premier Card. For more details on features visit https://www.google.com/'
        
        
        
        response_statement = Statement(text='{}.'.format(output))
        print('response_statement = ',response_statement)
        response_statement.confidence = 1
        
        return response_statement
    
    