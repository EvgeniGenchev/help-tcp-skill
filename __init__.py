from mycroft import MycroftSkill, intent_file_handler


class HelpTcp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tcp.help.intent')
    def handle_tcp_help(self, message):
        self.speak_dialog('tcp.help')


def create_skill():
    return HelpTcp()

