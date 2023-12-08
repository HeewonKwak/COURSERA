from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    wv = [[values[i], weights[i]] for i in range(len(weights))]
    for val, wei in sorted(wv, key= lambda x: -x[0]/x[1]):
        if wei <=capacity:
            capacity -= wei
            value += val
        else:
            value += capacity * val / wei
            break

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
