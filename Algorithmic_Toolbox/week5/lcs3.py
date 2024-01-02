def lcs3(first_sequence, second_sequence, third_sequence):
    dp = [[[0]*(len(first_sequence)+1) for _ in range(len(second_sequence)+1)]for _ in range(len(third_sequence)+1)]
    for i in range(1, len(third_sequence)+1):
        for j in range(1, len(second_sequence)+1):
            for k in range(1, len(first_sequence)+1):
                diff = 1 if third_sequence[i-1] == second_sequence[j-1] and second_sequence[j-1] == first_sequence[k-1] else 0
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1], dp[i-1][j-1][k], dp[i][j-1][k-1], dp[i-1][j][k-1], dp[i-1][j-1][k-1]+diff)
    return dp[len(third_sequence)][len(second_sequence)][len(first_sequence)]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
