from src.client.gui.dimensions import Position, Size
from src.client.mode import INSERT, NORMAL


class ModeWindow():
    """Represents mode info screen area
    (basically displays INSERT/NORMAL mode text"""

    def __init__(self, window):
        self.window = window
        self._mode = NORMAL
        self.pos = self.get_pos()
        self.size = self.get_size()

    def get_pos(self):
        """gets mode area pos"""
        win_y, win_x = self.window.getmaxyx()
        return Position(
                x=0,
                y=win_y
                )

    def get_size(self):
        """gets mode area size"""
        return Size(
                width=len(self.mode.text),
                height=1
                )

    def draw_mode_text(self):
        self.window.addstr(
                self.pos.y-1, self.pos.x,
                self._mode.text
                )

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        assert mode in (INSERT, NORMAL)
        self._mode = mode
