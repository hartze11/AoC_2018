#!/usr/bin/python

import itertools
filepath = 'd2-p1.txt'

data = []
count = 0

with open(filepath) as fp:
   line = fp.readline()
   while line:
       line = line.strip()
       #print(line)
       data.append(line)
       line = fp.readline()
       count += count

for a, b in itertools.combinations(data, 2):
    #print("{} {}").format(a, b)
    counter = 0
    score = 0
    for x in range(0, len(a)):
        if a[counter] == b[counter]:
            score += 1
        counter += 1
    if score >= 25:
        print("{} {} {}").format(a, b, score)
