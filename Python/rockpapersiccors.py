import random

choices =[]
choices.append("rock")
choices.append("paper")
choices.append("scissors")
oppochoice = random.choice(choices)




def coolintro(a):
	a
	game(choice)

def game(c):
	if c == oppochoice:
		print "We tied!"
	elif c != oppochoice:
		print "Let's go!"
		decision(choice, oppochoice)
	elif c != choices:
		print "Not cool dude! ;_;"
		coolintro(choice)
	

def decision(b,d):
	if b == choices[0] and d == choices[2] or b == choices[1] and d == choices[0] or b == choices[2] and d == choices[1]:
		print "Cool! You won!"
		b = ""
		d = random.choice(choices)
	else:
		print "You lost!"
		b = ""
		d = random.choice(choices)

def start():
	print oppochoice
	print "Pick rock, paper, or scissors!\t"
	choice = raw_input()
	coolintro(choice)



