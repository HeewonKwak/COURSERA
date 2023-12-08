def optimal_summands(n):
    summands = []
    # write your code here
    m = 1
    while 1:
        sum = (m + 1) * m // 2
        if sum == n:
            return [i for i in range(1, m+1)]
        elif sum > n:
            summands = [i for i in range(1, m)]
            summands[-1] += m - sum + n
            return summands
        m += 1


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
