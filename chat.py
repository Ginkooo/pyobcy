from collections import namedtuple

import config


class Chat():
    """recieve and send messages"""
    def __init__(self, drv):
        top_static = config.chat_top_static_info
        dynamic = config.chat_dynamic
        bottom_static = config.chat_bottom_static_info
        text_input = config.text_input
        self._top_static = self.drv.find_element_by_id(top_static)
        self._chat_area = self.drv.find_element_by_id(dynamic)
        self._bottom_static = self.drv.find_element_by_id(bottom_static)
        self._text_input = drv.find_element_by_id(text_input)

    def get_last_msg(self):
        """get last message (other's or yours)"""
        log_entry = config.message_entry_class
        elements = self.drv.find_elements_by_class_name(log_entry)
        last_msg = elements[-1].text
        sep = config.message_sep
        author, contents = last_msg.split(sep, 1)
        Message = namedtuple('Message', 'author contents')
        msg = Message(author=author, contents=contents)
        return msg
