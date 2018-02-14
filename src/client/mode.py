from collections import namedtuple


Mode = namedtuple('Mode', 'name text')
NORMAL = Mode(
        name='normal',
        text='(NORMAL)'
        )
INSERT = Mode(
        name='insert',
        text='(INSERT)'
        )
