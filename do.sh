#!/bin/bash
while [ true ]
do
	while read line
	do
	python ./get_data_multi.py $line
	done < "fail.txt"
	while read line
	do
	echo $line 
	#python ./get_data_multi.py $line
	done < "last_succ.txt"
done
