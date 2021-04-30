from mycroft import MycroftSkill, intent_file_handler
import socket
from datetime import datetime

HOST = '192.168.2.7'
PORT = 80
DEVICE_ID = 123653254

class HelpTcp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tcp.help.intent')
    def handle_tcp_help(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
            c.connect((HOST, PORT))
            alert = "Help " + str(DEVICE_ID) + " " + str(datetime.now())
            c.send(alert.encode('utf-8'))

        self.speak_dialog('tcp.help')


def create_skill():
    return HelpTcp()

