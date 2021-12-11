with open("./data/puzzle_three.txt") as f:
    lines = list(map(lambda x: x.replace("\n", ""), f.readlines()))
    
    vert_lines = [''.join(line) for line in zip(*[l.strip() for l in lines])]    
    
    count_tup = [[line.count('1'),line.count('0')] for line in vert_lines]
    most_common = ''.join([ '1' if tup[0]>tup[1] else '0' for tup in count_tup])
    less_common = ''.join([ '0' if tup[0]>tup[1] else '1' for tup in count_tup])
    
    print("Most:{}".format(int(most_common,2)))
    print("Less:{}".format(int(less_common,2)))
    print("Result:{}".format(int(most_common,2)*int(less_common,2)))

    oxy = lines.copy()
    for i in range(0,len(oxy[0]),1):
        temp_lines = list()
        vert_lines = [''.join(line) for line in zip(*[l.strip() for l in oxy])]
        count_tup = [[line.count('1'),line.count('0')] for line in vert_lines]
        if count_tup[i][0] == count_tup[i][1]:
            temp_lines = list(filter(lambda x: x[i] == '1',oxy))
        else:
            exp = '1' if count_tup[i][0] > count_tup[i][1] else '0'
            temp_lines = list(filter(lambda x: x[i] == exp ,oxy))
        oxy = temp_lines
        if len(oxy)<2:
            break
    print(int(''.join(oxy),2))
    
    co2 = lines.copy()
    for i in range(0,len(co2[0]),1):
        temp_lines = list()
        vert_lines = [''.join(line) for line in zip(*[l.strip() for l in co2])]
        count_tup = [[line.count('1'),line.count('0')] for line in vert_lines]
        if count_tup[i][0] == count_tup[i][1]:
            temp_lines = list(filter(lambda x: x[i] == '0',co2))
        else:
            exp = '1' if count_tup[i][0] < count_tup[i][1] else '0'
            temp_lines = list(filter(lambda x: x[i] == exp ,co2))
        co2 = temp_lines
        if len(co2)<2:
            break
    print(int(''.join(co2),2))
    print(int(''.join(co2),2)*int(''.join(oxy),2))