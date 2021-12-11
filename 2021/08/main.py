with open('data/puzzle_eight.txt') as f:
    lines = f.readlines()
    output_lines = list(map(lambda x: x.replace('\n', '').split('|')[1].strip().split(' '), lines))
    input_lines = list(map(lambda x: x.replace('\n', '').split('|')[0].strip().split(' '), lines))
    count = 0

for l in output_lines:
    count += len(list(filter(lambda y: len(y) == 4 or len(y) == 7 or len(y) == 2 or len(y) == 3, l)))

times = list()
for input, output_line in zip(input_lines,output_lines):
    # segment_wires = dict()
    one = [c for c in list(filter(lambda x: len(x) == 2, input))[0]]
    seven = [c for c in list(filter(lambda x: len(x) == 3, input))[0]]
    # print(seven)
    four = [c for c in list(filter(lambda x: len(x) == 4, input))[0]]
    eight = [c for c in list(filter(lambda x: len(x) == 7, input))[0]]
    # print(eight)
    five_two_three = [c for c in list(filter(lambda x: len(x) == 5, input))]
    zero_six_nine = [c for c in list(filter(lambda x: len(x) == 6, input))]
    six_filter = list(filter(lambda x: x not in seven, eight))
    nine_filter = four
    five_filter = list(filter(lambda x: x not in one, four))
    three_filter = one
    time_part = ""
    for p in output_line:
        if len(p) == 2:
            time_part += '1'
        if len(p) == 3:
            time_part += '7'
        if len(p) == 4:
            time_part += '4'
        if len(p) == 5:
            if all(c in p for c in three_filter):
                time_part += '3'
            elif all(c in p for c in five_filter):
                time_part += '5'
            else:
                time_part += '2'
        if len(p) == 6:
            if all(c in p for c in six_filter):
                time_part += '6'
            elif all(c in p for c in nine_filter):
                time_part += '9'
            else:
                time_part += '0'
        if len(p) == 7:
            time_part += '8'
    times.append(int(time_part))
print(sum(times))
