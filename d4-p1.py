import csv
import numpy as np
import time
import datetime

def unixtime(s):
    return time.mktime(datetime.datetime.strptime(s, "%m/%d/%Y").timetuple())

source = []

with open('d4-p1-ordered.csv', 'r') as csvfile:
    fn = csv.reader(csvfile, delimiter=' ')
    for row in fn:
      source.append(row)

del(source[0]) #  delete header line

sched = np.zeros( (1200,60) )

# s = source[0][0].split(',')[0]

for each in source:
    if 'Guard' in each[0]:
        guard = each[0].split(',')[4]
        begin = unixtime(each[0].split(',')[0])
        continue
    if 'asleep' in each[0]:
        asleep = unixtime(each[0].split(',')[0])
        continue
    if 'wakes' in each[0]:
        wake = unixtime(each[0].split(',')[0])
