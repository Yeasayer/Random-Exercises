import math,re

def factorial(num):
	j = 1
	newnum = num
	while (num-j > 0):
		newnum = newnum*(num-j)
		j = j+1
	return newnum
def start():
	print("Please enter a number greater than one")
	ournum = input("Your number here: ")
	if re.match(r'^([1-9][0-9]{1,}|[2-9])$',ournum):
		theAnswer = factorial(int(ournum))
	else:
		start()
	print("The Factorial of %s is %s" %(str(ournum),str(theAnswer)))
start()