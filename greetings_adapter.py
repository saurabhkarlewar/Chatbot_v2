from chatterbot.logic import LogicAdapter


class MyGreetingsAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['Hello', 'Hi', 'Hey','Howdy']
        if any(x in statement.text.lower().split() for x in words):
            return True
        else:
            return False
    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        #import requests
        import random
        responses = ['Hello', 'Hi there!', 'How are you','Greetings']
        response_statement = Statement(random.choice(responses))
        print('response_statement = ',response_statement)
        response_statement.confidence = 1
        return response_statement

