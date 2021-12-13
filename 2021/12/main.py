with open('data/puzzle_twelve.txt') as f:
    lines = list(map(lambda line: line, f.read().splitlines()))
points = [w.split('-') for w in lines]
start_points = list(filter(lambda x: 'start' in x, points))
end_points = list(filter(lambda x: 'end' in x, points))
waypoints = list(filter(lambda y: y not in start_points and y not in end_points, points))
start_points = [[x[0], x[1]] if x[0] in 'start' else [x[1], x[0]] for x in start_points]
end_points = [[x[1], x[0]] if x[0] in 'end' else [x[0], x[1]] for x in end_points]
print(start_points)
print(end_points)
print(waypoints)
result_way = list()
for s in start_points:
    for e in end_points:
        if s[1] in e[0]:
            w = ','.join(s)
            w += ',' + ','.join(e)
            result_way.append(w)
print(result_way)

# for s in start_points:
#     last_element = s
#     while(True):
#         filtered_way = list(filter(lambda x: s[1] in x, waypoints))
#         if len(filtered_way) < 1:
#             break