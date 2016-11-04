import re

for find in sorted(dir(re)):
	if ("find" in find):
		print find