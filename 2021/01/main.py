with open('data/puzzle_one.txt', 'r') as f:
    lines = list(map(lambda x: int(x.replace("\n", '')), f.readlines()))
    print("1.1: ", len(list(filter(lambda i: lines[i] < lines[i + 1], range(len(lines) - 2 + 1)))))
    lines = list(map(lambda i: lines[i] + lines[i + 1] + lines[i + 2], range(len(lines) - 3 + 1)))
    print("1.2: ", len(list(filter(lambda i: lines[i] < lines[i + 1], range(len(lines) - 2 + 1)))))