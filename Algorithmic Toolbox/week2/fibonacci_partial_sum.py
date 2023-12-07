# Uses python3

def fibonacci_partial_sum_naive(from_, to):
    return (fibonacci_sum(to) - fibonacci_sum(from_-1)) % 10

def fibonacci_sum(n):
    if n == 1:
        return n
    elif n < 1:
        return 0
    n = (n + 2) % 60
    a, b = 1, 0
    for i in range(2, n+1):
        a, b = (a + b) % 10, a
    return (a-1) % 10

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
