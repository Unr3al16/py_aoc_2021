def calc_median(list_of_values):
    n = len(list_of_values)
    if n % 2 == 0:
        return sorted(list_of_values)[n // 2]
    return sum(sorted(list_of_values)[n//2-1:n//2+1])/2

with open('data/puzzle_seven.txt') as f:
    crab_deep = list(map(lambda number: int(number), f.readline().split(',')))
    median = calc_median(crab_deep)
    print(sum([abs(i - median) for i in crab_deep]))

    comp_fuel = list()
    for i in range(2000):
        tmp_list = list()
        for c in crab_deep:
            steady_fuel = abs(c - i)
            tmp_list.append(int(0.5*steady_fuel*(steady_fuel+1)))
        comp_fuel.append(sum(tmp_list))
    print(min(comp_fuel))