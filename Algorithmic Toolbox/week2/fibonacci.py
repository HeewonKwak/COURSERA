# def fibonacci_number(n):
#     if n <= 1:
#         return n

#     return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonacci_number(n):
    if n <= 1:
        return n
    arr = [0 for _ in range(n+1)]
    arr[0], arr[1] = 0, 1
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
