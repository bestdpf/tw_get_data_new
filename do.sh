#!/bin/bash
while [ true ]
do
	read last_succ_id<"last_succ.txt"
	python get_data_bfs.py $last_succ_id
	echo "Restarting Python Sript"
done
