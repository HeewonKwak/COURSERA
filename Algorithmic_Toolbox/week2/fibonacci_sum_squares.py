def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    n = (n + 2) % 60
    a, b = 1, 0
    for i in range(2, n):
        a, b = (a + b) % 10, a
    return a * b % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
