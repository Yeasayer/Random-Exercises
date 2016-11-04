# Modify this function to return a list of strings as defined above
lister = []
lister.append("More organized code")
lister.append("More readable code")
lister.append("Easier code reuse")
lob = []
def list_benefits(a):
	for listen in a:
		print listen
		lob.append(listen)

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
	print "The benefit of functions are %s." % benefit

def name_the_benefits_of_functions():
    list_of_benefits = lister
    for benefit in list_of_benefits:
        print build_sentence(benefit)

print lister
list_benefits(lister)
name_the_benefits_of_functions()

 