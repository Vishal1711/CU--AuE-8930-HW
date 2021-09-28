def largestsum(nums):
    sumVal = 0
    ret = 0
    for i in nums:
        sumVal = max(0, sumVal) + i
        ret = max(ret, sumVal)
    return max(nums) if ret == 0 else ret

nums = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())

    nums.append(ele)


print('The largest sum is', largestsum(nums))
