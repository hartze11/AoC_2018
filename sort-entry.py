#!/usr/bin/python

filepath = 'd2-p1.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line = line.strip()
       line = ''.join(sorted(line))
       print(line)
       line = fp.readline()
