with open('data/puzzle_eleven.txt','r') as f:
# with open('data/test.txt', 'r') as f:
    energy = list(map(lambda line: [int(c) for c in line], f.read().splitlines()))
steps = 1
flashes = 0
synced = False
for i in range(10000):
    energy = list(map(lambda a: [s+1 for s in a], energy))
    if synced:
        print(i)
        break
    while(True):
        for y in range(len(energy)):
            y_down = -1 if y < 1 else y - 1
            y_up = y + 1 if y < len(energy) - 1 else - 1
            for x in range(len(energy[y])):
                if energy[y][x] > 9:
                    flashes += 1
                    energy[y][x] = -10000
                    x_left = -1 if x < 1 else x - 1
                    x_right = -1 if x == len(energy[y]) - 1 else x + 1
                    if y_up >= 0:
                        energy[y_up][x] += 1
                        if x_left >= 0:
                            energy[y_up][x_left] += 1
                        if x_right >= 0:
                            energy[y_up][x_right] += 1
                    if y_down >= 0:
                        energy[y_down][x] += 1
                        if x_left >= 0:
                            energy[y_down][x_left] += 1
                        if x_right >= 0:
                            energy[y_down][x_right] += 1
                    if x_right >= 0:
                        energy[y][x_right] += 1
                    if x_left >= 0:
                        energy[y][x_left] += 1
        if all(all([e <= 9 for e in l]) for l in energy):
            for y in range(len(energy)):
                for x in range(len(energy[y])):
                    if energy[y][x] < 0:
                        energy[y][x] = 0
            if all(all([e == 0 for e in l]) for l in energy):
                synced = True
            break
print(flashes)