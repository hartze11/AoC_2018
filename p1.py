import csv

file_list = []

with open('p1-input.csv') as csvfile:
    list = csv.reader(csvfile, delimiter=',')
    for row in list:
        file_list.append(int(row[0]))

#file_list = [+3, +3, +4, -2, -4]
# 10 is the first repeat

#file_list = [-6, +3, +8, +5, -6]
# should reach 5 first

# file_list = [7, +7, -2, -7, -4]
# 14

current = [0]
current_idx = 0

# create initial list
while current_idx < len(file_list):
    next = current[current_idx] + file_list[current_idx]
    current.append(next)
    current_idx = current_idx + 1

# Assume we need to repeat_list

found = False

while found is not True:
    file_idx = 0
    while file_idx < len(file_list):
        next = current[current_idx] + file_list[file_idx]
        if next in current:
            print("Found!: {}").format(next)
            current.append(next)
            found = True
            break
        else:
            print("Index {}. {} Not found, trying another digit").format(
                current_idx, next)
            current.append(next)
        current_idx = current_idx + 1
        file_idx = file_idx + 1
