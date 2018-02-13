import textwrap


class Drawer():
    def __init__(self, window):
        self.window = window
        self.lines = []
        self.messages = []
        self.resize_window()
        self.top_line = 0
        self.bottom_line = self.size[0] - 2

        self.redraw()

    def resize_window(self):
        size = self.window.getmaxyx()
        self.size = size[0]-1, size[1]-1

    def redraw(self):
        self._draw_chat_input_sep()
        self._draw_lines()

    def _draw_chat_input_sep(self):
        sep = '-' * self.size[1]
        sep_y = self.size[0] - 1
        sep_x = 0
        sep_pos = sep_y, sep_x
        self.window.addstr(*sep_pos, sep)

    def _draw_lines(self):
        disp_lines = self._get_disp_lines()
        if not disp_lines:
            return
        for i, line in enumerate(disp_lines):
            self.window.addstr(i, 0, ' '*(self.size[1] - 1))
            self.window.addstr(i, 0, line)

    def _get_disp_lines(self):
        if not self.lines:
            return None
        first = self.top_line
        last = self.bottom_line
        try:
            disp_lines = self.lines[first:last]
        except IndexError:
            disp_lines = self.lines[first:]
        return disp_lines

    def _conv_msg_to_lines(self, msg):
        msg = str(msg)
        lines = textwrap.wrap(msg, self.size[1] - 1)
        return lines

    def scroll(self, direction):
        if direction == 'down':
            self.top_line += 1
            self.bottom_line += 1
        elif direction == 'up':
            self.top_line -= 1
            self.bottom_line -= 1
        else:
            raise ValueError('Direction can be "up" or "down"')

    def add_message(self, msg):
        msg = str(msg)
        self.messages.append(msg)
        lines = self._conv_msg_to_lines(msg)
        self.lines.extend(lines)
