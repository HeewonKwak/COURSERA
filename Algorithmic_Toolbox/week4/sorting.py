from random import randint


def partition3(array, left, right):
    # write your code here
    l = left
    r = left
    u = right
    pivot = array[left]
    while r<=u:
        if array[r] < pivot:
            array[l], array[r] = array[r], array[l]
            l += 1
            r += 1
        elif array[r] > pivot:
            array[u], array[r] = array[r], array[u]
            u -= 1
        else:
            r += 1
    return l, r - 1

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
