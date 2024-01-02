from sys import stdin
from collections import defaultdict
from copy import deepcopy
from itertools import permutations

def partition3(values):
    target = sum(values) // 3
    if sum(values) % 3 != 0 or len(values) < 3:
        return 0
    idx = 0
    sum_case = defaultdict(list)
    sum_case[0] = []
    for idx, value in enumerate(values):
        ss = deepcopy(sum_case)
        for i in ss.keys():
            if i + value <= target:
                if i == 0:
                    sum_case[i + value].append([value])
                else:
                    for k in ss[i]:
                        sum_case[i + value].append(k + [value])
    if len(sum_case[target]) < 3:
        return 0
    for a, b, c in permutations(sum_case[target], 3):
        if sorted(values) == sorted(a+b+c):
            return 1
    return 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
