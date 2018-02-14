from src.client.gui.dimensions import Position, Size


class ChatWindow():
    """Represents chat area where message output is"""

    SEP_CHAR = '-'

    def __init__(self, window):
        self.window = window
        self.pos = self.get_pos()
        self.size = self.get_size()
        self.lines = []
        self._scroll_start = 0
        self._scroll_end = self.size.height - 1

    def get_size(self) -> Size:
        """get chat area size

        :rtype: Size
        """
        win_y, win_x = self.window.getmaxyx()
        chat_pos = self.get_pos()
        chat_y, chat_x = chat_pos.y, chat_pos.x
        size = Size(
                height=win_y - chat_y,
                width=win_x - chat_x
            )
        return size

    def get_pos(self) -> Position:
        """get chat area position

        :rtype: Position
        """
        return Position(
                x=0,
                y=0
                )

    def _draw_separator(self):
        """draw separator at the bottom of chat area"""
        sep_y, sep_x = (self.pos.y + self.size.height - 2,
                        self.pos.x + self.size.width - 1)
        sep = ChatWindow.SEP_CHAR * self.size.width
        self.window.addstr(sep_y, sep_x, sep)

    def clear_chat_area(self):
        """clears chat area by filling it with spaces"""
        for i in range(self.pos.y, self.pos.y + self.size.height - 1):
            self.clear_line(i)

    def clear_line(self, i):
        """clears line on index i

        :param i: line number to clear
        """
        spaces = ' ' * (self.size.width - 1)
        self.window.addstr(i, self.pos.x, spaces)

    def redraw_chat(self):
        """clears chat area and draws self.lines[start:end] onto chat area"""
        if not self.lines:
            return None
        self.clear_chat_area()
        try:
            lines = self.lines[self._scroll_start:self._scroll_end]
        except IndexError:
            lines = self.lines[self._scroll_start:]
        for i, line in enumerate(lines):
            y = i + self.pos.y
            x = self.pos.x
            self.window.addstr(y, x, line)

    def scroll(self, direction):
        """scrolls lines 'up' or 'down', does not redraw the screen"""
        assert direction in ('up', 'down')
        if direction == 'up':
            if self._scroll_start - 1 < 0:
                return None
            self._scroll_start -= 1
            self._scroll_end -= 1
        if direction == 'down':
            if len(self.lines) in range(self._scroll_start, self._scroll_end):
                return None
            self._scroll_start += 1
            self._scroll_end += 1
