def lcs2(first_sequence, second_sequence):
    dp = [[0]*(len(first_sequence)+1) for _ in range(len(second_sequence)+1)]
    for i in range(1, len(second_sequence)+1):
        for j in range(1, len(first_sequence)+1):
            diff = 1 if second_sequence[i-1] == first_sequence[j-1] else 0
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+diff)
    return dp[len(second_sequence)][len(first_sequence)]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m
    print(lcs2(a, b))
