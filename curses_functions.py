#Name: Aifric Nolan

import curses
import cmd
import os
import time
import curses
import sys
import subprocess

def enable_curses(stdscr):
	"""Enables you to collect character from keyboard and returns character"""
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(True)
	c = stdscr.getch() #Get key press
	return c

def disable_curses(stdscr):
	"""Disables curses """
	stdscr.keypad(False)
	curses.nocbreak()
	curses.echo()
	curses.endwin()