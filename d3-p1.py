import csv
import numpy as np

source = []

with open('d3-p1-clean.txt', 'r') as csvfile:
    fn = csv.reader(csvfile, delimiter=' ')
    for row in fn:
      source.append(row)

fabric = np.zeros( (1100,1100) )
common = 0

for each in source:
    start_x = int(each[1])
    start_y = int(each[2])
    elf = int(each[0])
    width = int(each[3])
    length = int(each[4])
    for x in range(start_x, (start_x + width)):
        # print x
        for y in range(start_y, (start_y + length)):
            # print y
            if fabric[x, y] == 0:
                fabric[x, y] = elf
                print("Setting {}, {} to Elf: {}.").format(x, y, elf)
            else:
                print("Setting {}, {} to COMMON 9999.").format(x, y)
                fabric[x, y] = 9999

total = (fabric == 9999).sum()

print total

counter = 0

for each in source:
    counter = 0
    start_x = int(each[1])
    start_y = int(each[2])
    elf = int(each[0])
    width = int(each[3])
    length = int(each[4])
    area = width * length
    for x in range(start_x, (start_x + width)):
        for y in range(start_y, (start_y + length)):
            if fabric[x, y] == elf:
                counter += 1
    if counter == area:
        print("Found ID: {}").format(elf)
