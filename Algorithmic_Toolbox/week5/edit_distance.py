def edit_distance(first_string, second_string):
    dp = [[float('INF') for _ in range(len(second_string)+1)] for _ in range(len(first_string)+1)]
    dp[0][0] = 0
    for j in range(len(second_string)+1):
        dp[0][j] = j
    for i in range(len(first_string)+1):
        dp[i][0] = i
    for i in range(1,len(second_string)+1):
        for j in range(1,len(first_string)+1):
            diff = 0 if first_string[j-1] == second_string[i-1] else 1
            dp[j][i] = min(dp[j-1][i] + 1, dp[j][i-1] + 1, dp[j-1][i-1] + diff)

    # print(dp)
    return dp[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
