with open('./data/puzzle_nine.txt') as f:
    lines = list(map(lambda line: [int(c) for c in line], f.read().splitlines()))
low_points = list()

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
        if all([x > cur_height for x in adjacents]):
            low_points.append(cur_height)
        adjacents = list()




        # for y in range(len(lines)):
#     y_down = len(lines) - 1 if y < 1 else y - 1
#     y_up = y + 1 if y < len(lines) - 1 else 0
#     for x in range(len(lines[y])):
#         x_left = len(lines[x]) - 1 if x < 1 else x - 1
#         x_right = 0 if x == len(lines[y]) - 1 else x + 1
#         cur_height = lines[y][x]
#         down = lines[y_down][x]
#         up = lines[y_up][x]
#         left = lines[y][x_left]
#         right = lines[y][x_right]
#         if cur_height < down and \
#             cur_height < up and \
#             cur_height < right and \
#             cur_height < left:
#             low_points.append(cur_height)
print(low_points)
print("First: {}".format(sum(map(lambda x: x + 1, low_points))))