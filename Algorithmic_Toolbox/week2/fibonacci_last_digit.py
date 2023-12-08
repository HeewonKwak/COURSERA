# import time

def fibonacci_last_digit(n):
    if n <= 1:
        return n
    a, b = 1, 0
    for _ in range(2,n+1):
        a, b = (a + b) % 10, a
        # print(a % 10)
    return a % 10


if __name__ == '__main__':
    n = int(input())
    # now = time.time()
    print(fibonacci_last_digit(n))
    # print(time.time() - now)