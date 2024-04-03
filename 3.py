## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

##You may assume that each input would have exactly one solution, and you may not use the same element twice.

##You can return the answer in any order.

def twoSum1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

def twoSum2(nums: list[int], target: int) -> list[int]:
    #sort
    sorted_nums = sorted(nums)
    mid = sorted_nums[len(sorted_nums) // 2]
    if target - mid:
        pass
    #get num at midpoint
    #maybe use recursion? divide and conquer?
    return

def twoSum3(nums: list[int], target: int) -> list[int]:
    def binary_search(lst, key):
        lo = 0
        hi = len(lst) - 1
        mid = (len(lst) - 1) // 2
        while lo <= hi:
            mid = (hi + lo) // 2
            if key == lst[mid]:
                return mid
            elif key > lst[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return None

    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        key = target - sorted_nums[i]
        res = binary_search(sorted_nums[i + 1:], key)
        if res != None:
            return [i, res+i+1]

def twoSum4(nums: list[int], target: int) -> list[int]:
    table = {}
    for i in range(len(nums)):
        table[nums[i]] = i

    for i in range(len(nums)):
        key = target - nums[i]
        j = table.get(key)
        if j != None and j != i:
            return [i, j]
lst1 = [2,7,11,15]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
lst3 = [3,2,4]
print(twoSum4(lst3, 6))
