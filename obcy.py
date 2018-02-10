import selenium.webdriver

import config
from chat import Chat
from location import Location


class DriverNotInitializedException(Exception):
    pass


class Obcy():
    """do things with 6Obcy"""

    def __init__(self, autoconnect=True, location=Location.LUBELSKIE):
        if autoconnect:
            self._init_driver()
            self._connect()
            self._choose_location(location)
            self._start_conversation()

    def _init_driver(self):
        """initialize webdriver"""
        self.drv = selenium.webdriver.Firefox()

    def _connect(self):
        """connect to 6obcy"""
        try:
            self.drv
        except AttributeError:
            raise DriverNotInitializedException()
        self.drv.get(config.url)

    def _choose_location(self, location):
        button = self.drv.find_element_by_id(config.location_button_id)
        button.click()
        spec_btn = self.drv.find_element_by_class_name(location)
        spec_btn.click()

    def _start_conversation(self):
        start_convo_btn = config.start_conversation_btn
        start_button = self.drv.find_element_by_id(start_convo_btn)
        start_button.click()

    def get_chat(self):
        chat = Chat(self.drv)
        return chat

    def close(self):
        """close connection to 60bcy"""
        try:
            self.drv.close()
        except AttributeError:
            raise DriverNotInitializedException()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
