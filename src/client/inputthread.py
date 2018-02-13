from threading import Thread
from queue import LifoQueue


class InputThread(Thread):

    def __init__(self, window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        window.nodelay(True)
        self.getch = window.getch
        self.char_queue = LifoQueue()
        self.stop = False

    def run(self):
        while not self.stop:
            char = self.getch()
            if char == -1:
                continue
            self.char_queue.put(char)

    def get_last_char(self):
        try:
            return self.char_queue.get_nowait()
        except:
            return None
