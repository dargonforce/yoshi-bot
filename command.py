from action import Action


class Command(object):
    def __init__(self, action: Action, help_text: str = ''):
        self.action = action
        self.help_text = help_text
