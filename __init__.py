from mycroft import MycroftSkill, intent_file_handler


class CurrentUser(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('user.current.intent')
    def handle_user_current(self, message):
        user = ''

        self.speak_dialog('user.current', data={
            'user': user
        })


def create_skill():
    return CurrentUser()

