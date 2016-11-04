a,b,c = 1,2,3
plus = a+b+c
minus = c-b-a
multi = a*b*c
divide = multi/plus
mathList = []
mathList.append(plus)
mathList.append(minus)
mathList.append(multi)
mathList.append(divide)
superList = mathList*10
if plus == multi:
	print (mathList)
	print (superList)
	print "\"mathList\" has %d objects!" % len(mathList)
	print "\"superList\" has %d objects!" % len(superList)
	print "Subtracting mathList from superList gives us %d objects!" % (len(superList) - len(mathList))