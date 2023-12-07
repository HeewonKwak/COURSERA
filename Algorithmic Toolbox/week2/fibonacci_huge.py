def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    arr = [0, 1]
    a, b = 1, 0
    for i in range(2,n+1):
        a, b = (a + b) % m, a % m
        arr.append(a)
        if a == 1 and b == 0:
            idx = n % (i - 1)
            return arr[idx]
    return a % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
