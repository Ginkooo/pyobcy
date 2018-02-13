from src.client.inputthread import InputThread


class Exit(Exception):
    pass


class InputHandler():
    def __init__(self, drawer):
        self.drawer = drawer
        self.input_thread = InputThread(drawer.window)
        self.input_thread.start()

    def react(self):
        char = self.input_thread.get_last_char()
        redraw = True
        if char == ord('q'):
            self.input_thread.stop = True
            self.input_thread.join()
            raise Exit()
        elif char == ord('k'):
            self.drawer.scroll('up')
        elif char == ord('j'):
            self.drawer.scroll('down')
        else:
            redraw = False
        return redraw
