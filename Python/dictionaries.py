phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781,
    "Jake" : 938273443
}

# write your code here
phonebook.pop("Jill")

# testing code

if "Jake" in phonebook:
   	print "Jake is listed in the phonebook. His phone number is %d!" % phonebook.get("Jake")
if "Jill" not in phonebook:
   	print "Jill is not listed in the phonebook. Yay!"