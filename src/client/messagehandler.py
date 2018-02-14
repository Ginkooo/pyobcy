class MessageHandler():
    """Responsible for telling Chat Window to print new messages
    and helps in redrawing messages due to terminal resize"""

    def __init__(self, chat_window):
        self.chat_window = chat_window
        self.messages = []

    def add_message(self, msg):
        """tell chat_window to print new message

        :param msg: Message to print
        """
        self.messages.append(msg)
        self.chat_window.print_msg(msg)
