from collections import namedtuple

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import config


class Chat():
    """recieve and send messages"""
    def __init__(self, drv):
        self.drv = drv
        top_static = config.chat_top_static_info
        dynamic = config.chat_dynamic
        bottom_static = config.chat_bottom_static_info
        text_input = config.text_input
        self._top_static = self.drv.find_element_by_id(top_static)
        self._chat_area = self.drv.find_element_by_id(dynamic)
        self._bottom_static = self.drv.find_element_by_id(bottom_static)
        self._text_input = drv.find_element_by_id(text_input)
        self._button = drv.find_element_by_class_name('first-button')
        self.msg_count = 0
        self.seen_msg_count = 0

    def get_msg_count(self):
        """count all messages"""
        log_entry = config.message_entry_class
        elements = self._chat_area.find_elements_by_class_name(log_entry)
        return len(elements)

    def get_last_msg(self):
        """get last message (other's or yours),
        return None, if there is no unseen msgs"""
        msg_count = self.get_msg_count()
        if msg_count == self.seen_msg_count:
            return
        log_entry = config.message_entry_class
        elements = self._chat_area.find_elements_by_class_name(log_entry)
        try:
            last_msg = elements[-1].text
        except IndexError:
            return
        sep = config.message_sep
        try:
            author, contents = last_msg.split(sep, 1)
        except:
            return
        Message = namedtuple('Message', 'author contents')
        msg = Message(author=author, contents=contents)
        self.seen_msg_count += 1
        return msg

    def send_msg(self, text):
        """send message on chat"""
        text_area = self.drv.find_element_by_id(config.text_input)
        text_area.send_keys(text)
        text_area.send_keys(Keys.RETURN)

    def get_status(self):
        """get conversation status basing on top_static"""
        try:
            end = self._bottom_static.find_element_by_class_name('log-static-end-talk')
        except NoSuchElementException:
            end = None
        try:
            writing = self._bottom_static.find_element_by_class_name('log-static-inner')
        except NoSuchElementException:
            writing = None
        if writing:
            return writing.text
        if end:
            return 'Disconnected'
        return self._top_static.text

    def start_new_conversation(self):
        """end current convo and start a new one"""
        for _ in range(3):
            self._button.click()
