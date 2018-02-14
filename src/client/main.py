import curses

from src.client.gui.chatwindow import ChatWindow
from src.client.gui.modewindow import ModeWindow
from src.client.gui.inputarea import InputArea
from src.client.gui.statuswindow import StatusWindow
from src.client.inputreader import InputReader
from src.client.messagehandler import MessageHandler
from src.client.mode import INSERT, NORMAL
from src.api.obcy import Obcy

obcy = Obcy()


def main(stdscr):
    chat = obcy.get_chat()
    chat_window = ChatWindow(stdscr)
    mode_window = ModeWindow(stdscr)
    status_window = StatusWindow(stdscr)
    input_area = InputArea(stdscr)
    message_handler = MessageHandler(chat_window)
    input_reader = InputReader(stdscr)
    chat_window._draw_separator()
    mode_window.draw_mode_text()
    while True:
        msg = chat.get_last_msg()
        status = chat.get_status()
        status_window.status = status
        status_window.draw()
        if msg:
            message_handler.add_message(msg)

            chat_window.redraw_chat()
            mode_window.draw_mode_text()
            input_area.draw_input_text()

        char = input_reader.read_next_char()
        if not char:
            continue
        if mode_window.mode == NORMAL:
            if char == ord('j'):
                chat_window.scroll('down')
            if char == ord('k'):
                chat_window.scroll('up')
            if char == ord('q'):
                break
            if char == ord('i'):
                mode_window.mode = INSERT
        else:
            if char == ord('`'):
                mode_window.mode = NORMAL
            elif char == curses.KEY_BACKSPACE:  # backspace
                input_area.backspace()
            elif char == ord('\n'):
                msg = input_area.text
                chat.send_msg(msg)
                input_area.erase()
            else:
                input_area.write_str(chr(char))

        chat_window.redraw_chat()
        mode_window.draw_mode_text()
        input_area.draw_input_text()


curses.wrapper(main)

obcy.close()
