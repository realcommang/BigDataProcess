#!/usr/bin/python3

w = open("output.txt", "wt")

with open(input(), "rt") as f:
	while True:
		text = f.read(1)
		if len(text) == 0: break
		if int(text) >= 97 && int(text) <= 122:
			w.write(char(int(text	
