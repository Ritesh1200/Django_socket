from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class MyConsumer(WebsocketConsumer):

    def connect(self):
        """
        it run when we connect
        """
        self.accept()
        self.send(text_data=json.dumps({"status": "connected woow" } ))
        

    def receive(self, text_data=None):
        """
        it run when we receive message
        """
        # Called with either text_data or bytes_data for each frame
        self.send(text_data=json.dumps({"status": "this is my returned message" }))
        


    def disconnect(self, close_code):
        """
        it run for break the connection
        """
        print("disconnected")