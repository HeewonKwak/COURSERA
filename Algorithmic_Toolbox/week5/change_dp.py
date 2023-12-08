def change(money):
    # write your code here
    dp = [float('INF') for _ in range(money+4)]
    dp[1] = 1
    dp[3] = 1
    dp[4] = 1
    coins = [1, 3, 4]
    for idx in range(1, money):
        dp[idx+1] = min(dp[idx] + 1, dp[idx+1])
        dp[idx+3] = min(dp[idx] + 1, dp[idx+3])
        dp[idx+4] = min(dp[idx] + 1, dp[idx+4])
    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
