from mycroft import MycroftSkill, intent_file_handler


class Wikidata(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wikidata.intent')
    def handle_wikidata(self, message):
        self.speak_dialog('wikidata')


def create_skill():
    return Wikidata()

