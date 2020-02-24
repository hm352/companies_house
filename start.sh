#!/usr/bin/env bash

while true
do
	PID=`cat /tmp/company_house.pid`

	if ps up $PID; then
		echo process is runinng
	    echo app already running at `date +%Y-%m-%d//%H:%M:%S` >> run_log.txt
	else
		echo starting main script
		echo app running at `date +%Y-%m-%d//%H:%M:%S` >> /app/run_log.txt
		python /app/main.py
	fi
done