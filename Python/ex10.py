tabby = "\tI'm tabbed in."
persian = "I'm split\non a line."
backslash = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby
print persian
print backslash
print fat_cat
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,