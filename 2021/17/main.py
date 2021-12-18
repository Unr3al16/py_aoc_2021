with open('data/puzzle_seventeen.txt') as fb:
    lines = fb.read().splitlines()
    target_x_start_stop = [int(_x) for _x in list(map(lambda __x:
                                                      __x.split(":")[1].strip().split(":")[0].split(',')[0].split("=")[
                                                          1].split('..'),
                                                      lines))[0]]
    target_y_start_stop = [int(_y) for _y in list(map(lambda __y:
                                                      __y.split(":")[1].strip().split(":")[0].split(',')[1].split("=")[
                                                          1].split('..'),
                                                      lines))[0]]
y_start = target_y_start_stop[1]
y_stop = target_y_start_stop[0]

x_start = target_x_start_stop[0]
x_stop = target_x_start_stop[1]

found_liste = list()
for x in range(0, 300, 1):
    for y in range(-150,300, 1):
        found = {}
        cur_position = [0, 0]
        velocity = [x, y]
        max_pos = -1
        in_target = False
        while (True):
            if velocity[0] >= 0:
                cur_position[0] += velocity[0]
            cur_position[1] += velocity[1]
            if cur_position[1] > max_pos:
                max_pos = cur_position[1]
            velocity[0] -= 1
            velocity[1] -= 1
            if x_start <= cur_position[0] <= x_stop and y_start >= cur_position[1] >= y_stop:
                in_target = True
            if cur_position[1] < y_stop - 5:
                break
        if in_target:
            found['vel_x'] = x
            found['vel_y'] = y
            found['max'] = max_pos
            found_liste.append(found)

# print("Found in target: {}".format(in_target))
print('Targets: {}'.format( max(found_liste, key=lambda x: x['max'])))
print(len(found_liste))