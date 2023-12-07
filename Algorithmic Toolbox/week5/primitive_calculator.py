def compute_operations(n):
    answer = []
    dp = [float('INF') for _ in range(3*n+1)]
    dp[1] = 1
    for i in range(1, n):
        dp[i+1] = min(dp[i+1], dp[i]+1)
        dp[i*2] = min(dp[i*2], dp[i]+1)
        dp[i*3] = min(dp[i*3], dp[i]+1)
    idx = n
    answer.append(n)
    cnt = dp[n]
    while 1:
        if cnt - 1 == dp[idx-1]:
            answer.append(idx-1)
            idx -= 1
        elif cnt - 1 == dp[idx//2] and idx % 2 == 0:
            answer.append(idx//2)
            idx //= 2
        elif cnt - 1 == dp[idx//3] and idx % 3 == 0:
            answer.append(idx//3)
            idx //= 3
        cnt -= 1
        if dp[idx] == 1:
            break
    return answer[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
