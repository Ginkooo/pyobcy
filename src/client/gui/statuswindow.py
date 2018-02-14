from src.client.gui.dimensions import Position, Size


class StatusWindow():
    """Conversation status in top of the screen"""

    def __init__(self, window):
        self.window = window
        self.pos = self.get_pos()
        self.size = self.get_size()
        self._status = 'Disconnected'
        self._prev_status = ''

    def get_pos(self):
        return Position(
                x=0,
                y=0
                )

    def get_size(self):
        _, win_x = self.window.getmaxyx()
        return Size(
                width=win_x,
                height=1
                )

    def draw(self):
        """draw status on screen"""
        if self._status == self._prev_status:
            return
        y, x = self.pos.y, self.pos.x
        self.window.addstr(y, x, self.status)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._prev_status = self.status
        self._status = status
