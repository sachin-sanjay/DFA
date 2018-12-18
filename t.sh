#!/bin/bash
#make sure to source the workspace with the video file
while [ 1 ]
do
	d=$(curl POST -d '{"lol":"lol"}' http://127.0.0.1:5000/auth)
	echo "$d"
	if [ "$d" = "1" ]; then
		roslaunch main dfa.launch
	fi
	sleep 2
done
