def binary_search(keys, query, start, end):
    # write your code here
    mid = (start + end)//2
    if start >end:
        return -1
    if keys[mid] == query:
        return mid
    elif keys[mid] < query:
        return binary_search(keys, query, mid + 1, end)
    elif keys[mid] > query:
        return binary_search(keys, query, start, mid - 1)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q, 0, num_keys-1), end=' ')
