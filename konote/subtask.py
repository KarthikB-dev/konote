import curses
from curses import wrapper

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# TODO take input to add subtasks

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
