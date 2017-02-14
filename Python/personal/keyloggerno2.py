

# Help from http://stackoverflow.com/questions/13207678/whats-the-simplest-way-of-detecting-keyboard-input-in-python-from-the-terminal

global isWindows

isWindows = False
try:
	from win32api import STD_INPUT_HANDLE
	from win32console import GetStdHandle, KEY_EVENT, ENABLE_ECHO_INPUT, ENABLE_LINE_INPUT, ENABLE_PROCESSED_INPUT
	print("Using Windows libraries!")
    isWindows = True
except ImportError as e:
	print("Using Unix libraries!")
	import sys, select, termios, time

#first time using a class albeit typed-pasted:
class KeyPoller():
	def __enter__(self):
		global isWindows
		if isWindows:
			self.readHandle = GetStdHandle(STD_INPUT_HANDLE)
            self.readHandle.SetConsoleMode(ENABLE_LINE_INPUT|ENABLE_ECHO_INPUT|ENABLE_PROCESSED_INPUT)

            self.curEventLength = 0
            self.curKeysLength = 0

            self.capturedChars = []
		else:
			self.fd = sys.stdin.fileno()
			self.new_term = termios.tcgetattr(self.fd)
			self.old_term = termios.tcgetattr(self.fd)