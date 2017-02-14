import sys, select, time

# Help from http://stackoverflow.com/questions/13207678/whats-the-simplest-way-of-detecting-keyboard-input-in-python-from-the-terminal

def keyEnter():
	i,o,e = select.select([sys.stdin],[],[],0.0001)
	print(i,sys.stdin)
	for s in i:
		print(s)



while 1:
	print(select.select([sys.stdin], [], [], 0)[0])
	#keyEnter()
