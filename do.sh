#!/bin/bash
while [ true ]
do
	while read line
	do
	echo $line 
	python ./get_data_multi.py $line
	done < "last_succ.txt"
done
