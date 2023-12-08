def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = ''
    nums = []
    for num in numbers:
        nums.append([num, num+num[0]*(4-len(num))])

    for i, _ in sorted(nums, key=lambda x:(x[1],x[0][-1]), reverse=True):
        largest += i

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
