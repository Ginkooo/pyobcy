import curses
from src.client.gui.chatwindow import ChatWindow
from src.client.gui.modewindow import ModeWindow
from src.client.inputreader import InputReader


def main(stdscr):
    chat_window = ChatWindow(stdscr)
    mode_window = ModeWindow(stdscr)
    input_reader = InputReader(stdscr)
    chat_window._draw_separator()
    chat_window.lines = [f'dupa {i}' for i in range(100)]
    chat_window.redraw_chat()
    mode_window.draw_mode_text()
    while True:
        char = input_reader.read_next_char()
        if not char:
            continue
        if char == ord('j'):
            chat_window.scroll('down')
        if char == ord('k'):
            chat_window.scroll('up')
        if char == ord('q'):
            exit()

        chat_window.redraw_chat()
        mode_window.draw_mode_text()


curses.wrapper(main)
