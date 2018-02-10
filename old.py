from collections import namedtuple
from threading import Thread

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://6obcy.com.pl'
location_button_id = 'intro-interface-location-button'
specific_loation_class_name = 'location-id-6'
start_convo_btn = 'intro-start'
text_input = 'box-interface-input'

msg_count = 0
last_msg = ''


def connect():
    drv = webdriver.Firefox()
    drv.get(url)
    return drv


def choose_location(drv):
    button = drv.find_element_by_id(location_button_id)
    button.click()
    lubbutton = drv.find_element_by_class_name(specific_loation_class_name)
    lubbutton.click()


def start_convo(drv):
    start_button = drv.find_element_by_id(start_convo_btn)
    start_button.click()


def get_text_input(drv):
    textarea = drv.find_element_by_id(text_input)
    return textarea


def get_chat(drv):
    top_static = drv.find_element_by_id('log-static-top')
    chat_area = drv.find_element_by_id('log-dynamic')
    bottom_static = drv.find_element_by_id('log-static')
    text_input = get_text_input(drv)
    chat = namedtuple('Chat', 'top_static chat_area botton_static text_input')
    chat.top_static = top_static
    chat.chat_area = chat_area
    chat.botton_static = bottom_static
    chat.text_input = text_input
    return chat


def get_last_msg(area):
    global msg_count
    elements = area.find_elements_by_class_name('log-entry')
    msg_count = len(elements)
    last = elements[-1]
    return last.text


def send_msg(msg, textinput):
    textinput.sendkeys(msg)
    textinput.sendkeys(Keys.RETURN)


def print_new_messages(chat):
    global last_msg
    tmp_msg_count = 0
    while True:
        msg = get_last_msg(chat.chat_area)
        if not (msg == last_msg and tmp_msg_count == msg_count):
            print()
            print(msg)
        last_msg = msg
        tmp_msg_count = msg_count


drv = connect()
choose_location(drv)
start_convo(drv)
chat = get_chat(drv)
while not chat.top_static.text.startswith('Rozpocz'):
    pass

while not chat.chat_area.text:
    pass

print_thread = Thread(target=print_new_messages, args=(chat,))
print_thread.run()

drv.close()
