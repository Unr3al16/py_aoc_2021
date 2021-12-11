with open('data/puzzle_six.txt') as f:
    state = list(map(lambda number: int(number), f.readline().split(',')))
    cnt_dict = dict()
    for n in state:
        if n not in cnt_dict.keys():
            cnt_dict[n] = 0
        cnt_dict[n] += 1

    for i in range(256):
        tmp_cnt = dict()
        for k in cnt_dict.keys():
            if k != 0:
                if k-1 not in tmp_cnt.keys():
                    tmp_cnt[k-1] = 0
                tmp_cnt[k-1] += cnt_dict[k]
            else:
                if 6 not in tmp_cnt.keys():
                    tmp_cnt[6] = 0
                tmp_cnt[6] += cnt_dict[k]
                if 8 not in tmp_cnt.keys():
                    tmp_cnt[8] = 0
                tmp_cnt[8] += cnt_dict[k]
        cnt_dict = tmp_cnt
    print(sum([v for k,v in cnt_dict.items()]))


