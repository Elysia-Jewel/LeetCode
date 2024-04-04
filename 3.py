## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

##You may assume that each input would have exactly one solution, and you may not use the same element twice.

##You can return the answer in any order.

def twoSum1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

def twoSum2(nums: list[int], target: int) -> list[int]:
    table = {}
    for i in range(len(nums)):
        table[nums[i]] = i

    for i in range(len(nums)):
        key = target - nums[i]
        j = table.get(key)
        if j != None and j != i:
            return [i, j]

def twoSum3(nums: list[int], target: int) -> list[int]:
    table = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in table:
            return [table[diff], i]
        table[num] = i

def twoSum4(nums: list[int], target: int) -> list[int]:
    table = {}
    for num in nums:
        diff = target - num
        if diff in table:
            return [table[diff], nums.index(num)] 
            #does not work because index() returns the index of the first occurence of the element, not the index of the current occurence of the element
        table[num] = nums.index(num)

def twoSum4fixed(nums: list[int], target: int) -> list[int]:
    table = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in table:
            return [table[diff], i]
        else:
            table[nums[i]] = i


lst1 = [2,7,11,15]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]
lst3 = [3,2,4]
lst4 = [3, 3]
print(twoSum4fixed(lst4, 6))
