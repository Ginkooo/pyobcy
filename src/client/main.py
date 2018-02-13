import curses

from src.client.drawer import Drawer
from src.client.inputthread import InputThread
from src.client.inputhandler import InputHandler, Exit


def main(stdscr):
    drawer = Drawer(stdscr)
    msgs = (f'dupa {i}' * 22 for i in range(10000))
    for msg in msgs:
        drawer.add_message(msg)
    input_handler = InputHandler(drawer)
    drawer.redraw()
    is_changed = False
    while True:
        if is_changed:
            drawer.redraw()
        try:
            is_changed = input_handler.react()
        except Exit:
            break


curses.wrapper(main)
