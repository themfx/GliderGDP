#!/bin/bash

# Because I always forget the commands
#  and this is easier

echo "WARNING: all changes will be committed and pushed"

echo "Type the message to accompany this commit:"
read message

echo "Setting commit with this message:" $message
git add -A
git rm --cached -r *.pyc
git rm --cached Tools/Missions/*.txt
git commit -m "$message"

echo "Pushing to master"
git push origin master

echo "All complete - PushMaster.sh ending"
