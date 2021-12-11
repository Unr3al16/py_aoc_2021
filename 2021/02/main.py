with open('data/puzzle_two.txt', 'r') as f:
    lines = list(map(lambda x: x.replace("\n", '').split(' '), f.readlines()))
    forw = sum(list(map(lambda l: int(l[1]), filter(lambda x: x[0] == 'forward', lines))))
    up = -sum(list(map(lambda l: int(l[1]), filter(lambda x: x[0] == 'up', lines))))
    down = sum(list(map(lambda l: int(l[1]), filter(lambda x: x[0] == 'down', lines))))
    print("2.1: ", forw * (up + down))
    aim = 0
    deep = 0
    for line in lines:
        if line[0] == "forward":
            deep += aim * int(line[1])
        elif line[0] == "up":
            aim -= int(line[1])
        elif line[0] == "down":
            aim += int(line[1])
    print("2.2: ", forw * deep)
