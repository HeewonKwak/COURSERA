from sys import stdin


def maximum_gold(capacity, weights):
    dp = [{0}]
    for idx, weight in enumerate(weights):
        case = set()
        for i in dp[idx]:
            case.add(i)
            if i + weight <= capacity:
                case.add(i+weight)
        dp.append(case)
    return max(dp[-1])


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
