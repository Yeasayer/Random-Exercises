from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying %s to %s" % (from_file, to_file),

# I can do these two on one line.
indata = open(from_file).read()

print "Ready, hit RETURN to continue, CTRL-C (^C) to abort."
raw_input()

out_file = open(to_file, 'w'); out_file.write(indata)

print "Alright, all done!"

out_file.close();