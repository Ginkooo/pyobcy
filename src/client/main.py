import curses

from src.client.gui.chatwindow import ChatWindow
from src.client.gui.modewindow import ModeWindow
from src.client.gui.inputarea import InputArea
from src.client.inputreader import InputReader
from src.client.mode import INSERT, NORMAL


def main(stdscr):
    chat_window = ChatWindow(stdscr)
    mode_window = ModeWindow(stdscr)
    input_area = InputArea(stdscr)
    input_reader = InputReader(stdscr)
    chat_window._draw_separator()
    chat_window.lines = [f'dupa {i}' for i in range(100)]
    chat_window.redraw_chat()
    mode_window.draw_mode_text()
    while True:
        char = input_reader.read_next_char()
        if not char:
            continue
        if mode_window.mode == NORMAL:
            if char == ord('j'):
                chat_window.scroll('down')
            if char == ord('k'):
                chat_window.scroll('up')
            if char == ord('q'):
                exit()
            if char == ord('i'):
                mode_window.mode = INSERT
        else:
            if char == ord('`'):
                mode_window.mode = NORMAL
            elif char == ord('\n'):
                msg = input_area.text
                input_area.erase()
            else:
                input_area.write_str(chr(char))

        chat_window.redraw_chat()
        mode_window.draw_mode_text()
        input_area.draw_input_text()


curses.wrapper(main)
