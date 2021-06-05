from mycroft import MycroftSkill, intent_file_handler


class LeaveEntitlements(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('entitlements.leave.intent')
    def handle_entitlements_leave(self, message):
        self.speak_dialog('entitlements.leave')


def create_skill():
    return LeaveEntitlements()

