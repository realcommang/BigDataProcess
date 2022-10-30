#!/usr/bin/python3

import sys

genres = dict() 
with open(sys.argv[1], "r") as f:
	list = f.readlines()
	for i in list:
		grs = i.split("::")[2]
		grsList = grs.split("|")
		for g in grsList:
			g = g.replace("\n", "")
			if g in genres:
				genres[g] += 1
			else:
				genres[g] = 1

with open(sys.argv[2], "w") as f:
	for key, value in genres.items():
		f.write(key + " " + str(value) + "\n")
