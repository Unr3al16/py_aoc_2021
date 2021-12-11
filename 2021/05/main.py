import re

with open('data/puzzle_five.txt') as f:
    lines = list(map(lambda l: re.split(',| -> ', l.replace('\n','')), f.readlines()))
    lines = list(filter(lambda x: x[0] == x[2] or
                                  x[1] == x[3] or
                                  abs(int(x[0])-int(x[2])) == abs(int(x[1])-int(x[3])) ,lines))
    f.close()
x =  1000
vent_map= [[ 0 for x in range(x)] for y in range(x)]
for vent in lines:
    if vent[0] == vent[2]:
        s = int(vent[0])
        start = int(vent[1]) if int(vent[1]) < int(vent[3]) else int(vent[3])
        stop = int(vent[3]) if int(vent[1]) < int(vent[3]) else int(vent[1])
        for i in range(start, stop+1, 1):
            vent_map[s][i] += 1
    elif vent[1] == vent[3]:
        s = int(vent[1])
        start = int(vent[0]) if int(vent[0]) < int(vent[2]) else int(vent[2])
        stop = int(vent[2]) if int(vent[0]) < int(vent[2]) else int(vent[0])
        for i in range(start, stop+1, 1):
            vent_map[i][s] += 1
    else:
        x1 = int(vent[0])
        x2 = int(vent[2])
        y1 = int(vent[1])
        y2 = int(vent[3])
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        for i in range(x1, x2 + x_step,x_step):
            if y1 != y2 + y_step:
                vent_map[i][y1] += 1
                y1 += y_step


count = 0
for x in vent_map:
    count += len(list(filter(lambda v: v >= 2, x)))

print(count)