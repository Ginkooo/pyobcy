class InputReader():
    """Reads and handles user input"""
    def __init__(self, window):
        self.window = window
        window.nodelay(True)

    def read_next_char(self):
        char = self.window.getch()
        if char == -1:
            return None
        return char
