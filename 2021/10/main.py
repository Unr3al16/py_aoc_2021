with open('./data/puzzle_ten.txt') as f:
    brackets = list(map(lambda line: [c for c in line], f.read().splitlines()))
open_brackets = ['[','(','<','{']
bracket_pairs = {
    ']': '[',
    ')': '(',
    '>': '<',
    '}': '{'}
failure_bracket_points = {
    ']': 57,
    ')': 3,
    '>': 25137,
    '}': 1197}
incomplete_bracket_points = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}
last_open_brackets = list()
failure_brackets = list()
incomplete_list = list()
failure = False
for line in brackets:
    for bracket in line:
        current_bracket = bracket
        if bracket in open_brackets:
            last_open_brackets.append(bracket)
        elif last_open_brackets[-1] == bracket_pairs[bracket]:
            last_open_brackets.pop()
        elif last_open_brackets[-1] != bracket_pairs[bracket]:
            # print(bracket)
            failure = True
            failure_brackets.append(bracket)
            break
    if not failure:
        incomplete_list.append(line)
    else:
        failure = False
    last_open_brackets = list()
print(sum([failure_bracket_points[f] for f in failure_brackets]))
line_values = []
for line in incomplete_list:
    for bracket in line:
        current_bracket = bracket
        if bracket in open_brackets:
            last_open_brackets.append(bracket)
        elif last_open_brackets[-1] == bracket_pairs[bracket]:
            last_open_brackets.pop()
    partial_sum = 0
    last_open_brackets.reverse()
    for bracket in last_open_brackets:
        for k, v in bracket_pairs.items():
            if bracket == v:
                partial_sum = partial_sum * 5
                partial_sum += incomplete_bracket_points[k]
    line_values.append(partial_sum)
    last_open_brackets = list()
line_values.sort()
mid = int(len(line_values)/2)
print(line_values[mid])