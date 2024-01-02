from sys import stdin
from collections import defaultdict


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)
    horizon = []
    point_cnt = defaultdict(list)

    sp, pp, ep = 0, 1, 2
    for s in starts:
        horizon.append([s, sp])
    for idx, p in enumerate(points):
        horizon.append([p, pp])
        point_cnt[p].append(idx)
    for e in ends:
        horizon.append([e, ep])

    horizon.sort(key=lambda x: (x[0], x[1]))

    cnt = 0
    for point in horizon:
        if point[1] == 0:
            cnt += 1
        elif point[1] == 2:
            cnt -= 1
        else:
            idx_list = point_cnt[point[0]]
            for ii in idx_list:
                count[ii] = cnt

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)
