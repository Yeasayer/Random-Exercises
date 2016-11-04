#!/bin/sh

COMMIT_MESSAGE=$1
TEST_VALUE=input

git add .
if ["$COMMIT_MESSAGE" == ""]
	then
	echo "Okay what do you want as your commit message?\n"
	read input
	COMMIT_MESSAGE=$input
	echo $COMMIT_MESSAGE
git commit -m "$COMMIT_MESSAGE"
fi
echo "Okay, we're pushing to master!\n"
git push origin master
echo "AWESOME! We're done here!\n"