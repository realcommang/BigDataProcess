#!/usr/bin/python3

import sys
import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
ubers = []
count = 0

with open(sys.argv[1], "r") as f:
	lines = f.readlines()
	for l in lines:
		line = l.split(",")
		date = line[1].split("/")
		line[1] = days[datetime.date(int(date[2]), int(date[0]), int(date[1])).weekday()]
		line[3] = line[3].replace("\n", "")
		line[2] = int(line[2])
		line[3] = int(line[3])
		count = 0
		for u in ubers:
			if (u[0] == line[0]) and (u[1] == line[1]):
				u[2] += line[2]
				u[3] += line[3]
				count = 1
	
		if count == 0:
			ubers.append(line)
	
with open(sys.argv[2], "w") as f:
	for u in ubers:
		f.write(u[0] + "," + u[1] + " " + str(u[2]) + "," + str(u[3]) + "\n") 
