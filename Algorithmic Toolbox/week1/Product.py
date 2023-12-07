# Maximum Pairwise Product

def maximum_Pairwise_Product(nums):
    max_idx1 = -1
    max_idx2 = -1
    max_val = -1
    for i in range(len(nums)):
        if nums[i] > max_val:
            max_idx1 = i
            max_val = nums[i]
    
    max_val = -1
    for i in range(len(nums)):
        if nums[i] > max_val and i != max_idx1:
            max_idx2 = i
            max_val = nums[i]

    # print(max_idx1, max_idx2)
    
    return nums[max_idx1] * nums[max_idx2]

n = int(input())

nums = list(map(int, input().split()))

print(maximum_Pairwise_Product(nums))