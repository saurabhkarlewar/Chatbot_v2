from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import get_response
import logging

class ChatServer(WebSocket):
    logging.basicConfig(level=logging.INFO)
    def handleMessage(self):
        # echo message back to client
        message = self.data
        print(message)
        response = get_response(message)
        print(response)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()