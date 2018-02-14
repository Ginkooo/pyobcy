from src.client.gui.dimensions import Position, Size
from src.client.mode import INSERT, NORMAL


class InputArea():
    """area where you can type messages"""

    def __init__(self, window):
        self.window = window
        self.pos = self.get_pos()
        self.size = self.get_size()
        self.text = ''

    def get_size(self):
        """get input area size"""
        _, win_x = self.window.getmaxyx()
        return Size(
                width=win_x - self.pos.x,
                height=1
                )

    def get_pos(self):
        """get input are pos"""
        win_y, win_x = self.window.getmaxyx()
        mode_len = max(len(INSERT.text), len(NORMAL.text))
        return Position(
                x=mode_len + 1,
                y=win_y-1
                )

    def draw_input_text(self):
        x, y = self.pos.x, self.pos.y
        if not self.text:
            spaces = ' ' * (self.size.width - 1)
            self.window.addstr(y, x, spaces)
            return None
        try:
            self.window.addstr(y, x, self.text)
        except:
            raise Exception(y, x, self.text)

    def erase(self):
        self.text = ''

    def write_str(self, str):
        self.text += str
