def find_on_x(x, y, sea_map):
    coords = set()
    _x = x
    _y = y
    while(True):
        _x += 1
        if _x == len(sea_map[y]):
            break
        t = sea_map[_y][_x]
        if sea_map[_y][_x] == 9:
            break
        for i in range(_y, 0, -1):
            t = sea_map[i][_x]
            if sea_map[i][_x] == 9:
                break
            else:
                coords.add((_x, i))
        for i in range(_y, len(sea_map), 1):
            t = sea_map[i][_x]
            if sea_map[i][_x] == 9:
                break
            else:
                coords.add((_x, i))
    _x = x
    _y = y
    while (True):
        _x -= 1
        if _x < 0:
            break
        g = sea_map[_y][_x]
        if sea_map[_y][_x] == 9:
            break
        for i in range(_y, 0, -1):
            g = sea_map[i][_x]
            if sea_map[i][_x] == 9:
                break
            else:
                coords.add((_x, i))
        for i in range(_y, len(sea_map), 1):
            t = sea_map[i][_x]
            if sea_map[i][_x] == 9:
                break
            else:
                coords.add((_x, i))
    return coords

def find_on_y(x, y, sea_map):
    coords = set()
    _x = x
    _y = y
    while(True):
        _y += 1
        if _y == len(sea_map):
            break
        if sea_map[_y][_x] == 9:
            break
        for i in range(_x, 0, -1):
            if sea_map[_y][i] == 9:
                break
            else:
                coords.add((i, _y))
        for i in range(_x, len(sea_map[0]), 1):
            if sea_map[_y][i] == 9:
                break
            else:
                coords.add((i, _y))
    _x = x
    _y = y
    while (True):
        _y -= 1
        if _y <  0:
            break
        if sea_map[_y][_x] == 9:
            break
        for i in range(_x, 0, -1):
            if sea_map[_y][i] == 9:
                break
            else:
                coords.add((i, _y))
        for i in range(_x, len(sea_map), 1):
            if sea_map[_y][i] == 9:
                break
            else:
                coords.add((i, _y))
    return coords

with open('./data/test.txt') as f:
    lines = list(map(lambda line: [int(c) for c in line], f.read().splitlines()))
low_points = list()
low_points_coords = list()
basin_size = list()
for y in range(len(lines)):
    adjacents = list()
    y_down = -1 if y < 1 else y - 1
    y_up = y + 1 if y < len(lines) - 1 else - 1
    for x in range(len(lines[y])):
        x_left = -1 if x < 1 else x - 1
        x_right = -1 if x == len(lines[y]) - 1 else x + 1
        cur_height = lines[y][x]
        if x_left >= 0: adjacents.append(lines[y][x_left])
        if x_right >= 0: adjacents.append(lines[y][x_right])
        if y_up >= 0: adjacents.append(lines[y_up][x])
        if y_down >= 0: adjacents.append(lines[y_down][x])
        if all([s > cur_height for s in adjacents]):
            low_points.append(cur_height)
            low_points_coords.append((cur_height, x, y))
        adjacents = list()
adjacents = list()
test_adjacents = list()
for p in low_points_coords:
    counter_set = set()
    start_x = p[1]
    start_y = p[2]
    counter_set.add((start_x, start_y))
    counter_set.update(find_on_x(start_x, start_y, lines))
    counter_set.update(find_on_y(start_x, start_y, lines))
    adjacents.append(len(counter_set))
    test_adjacents.append((p, len(counter_set)))



print(low_points)
print("First: {}".format(sum(map(lambda x: x + 1, low_points))))
adjacents.sort()
print(adjacents)
print("Second: {}".format(adjacents[-1]*adjacents[-2]*adjacents[-3]))