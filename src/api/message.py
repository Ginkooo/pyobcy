class Message():
    """represents message"""
    def __init__(self, author, contents):
        self.author = author
        self.contents = contents

    def __str__(self):
        return f'{self.author self.contents}'
