import re


def print_card(card_list):
    for y in range(len(card_list)):
        s = " ".join(card_list[y])
        print(s)


def count(cards):
    counter = 0
    for y in range(0, len(cards), 1):
        for x in range(0, len(cards[0]), 1):
            if cards[y][x] is '#':
                counter += 1
    return counter


def run(res, times=-1):
    for f in folding:
        if times == 0:
            break
        times -= 1
        axe = f.split('=')[0]
        folding_line = int(f.split('=')[1])
        if axe is 'y':
            tmp = res[folding_line + 1:]
            res = res[:folding_line]
            for y in range(len(tmp), 0, -1):
                for x in range(0, len(tmp[0]), 1):
                    if res[len(res) - y][x] is '.':
                        res[len(res) - y][x] = tmp[y - 1][x]
        if axe is 'x':
            tmp = [y[folding_line + 1:] for y in res]
            res = [y[:folding_line] for y in res]
            for x in range(len(tmp[0]), 0, -1):
                for y in range(0, len(tmp), 1):
                    if res[y][len(res[0]) - x] is '.':
                        res[y][len(res[0]) - x] = tmp[y][x - 1]
    return res


with open("data/puzzle_thirteen.txt", 'r') as fs:
    lines = fs.read().splitlines()
    coordinates = [[int(s[0]), int(s[1])] for s in list(map(lambda y: y.split(','),
                                                            filter(lambda x: re.match("[0-9+]+,[0-9]+", x), lines)))]
    x_max = max(list(map(lambda x: x[0], coordinates))) + 1
    y_max = max(list(map(lambda y: y[1], coordinates))) + 1
    folding = list(map(lambda x: x.split(' ')[-1],
                       filter(lambda x: re.match("[a-z]*\\s[a-z]*\\s[a-z]=[0-9]", x), lines)))
card = [['.' for x in range(x_max)] for y in range(y_max)]
for x, y in coordinates:
    card[y][x] = '#'

print("Part 1: {}".format(count(run(card, 1))))
print("Part 2:")
print_card(run(card))

