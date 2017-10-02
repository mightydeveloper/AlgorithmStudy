def twoSum(nums, target):
    need = {}
    for i, num in enumerate(nums):
	if num in need:
	    return need[num], i
	need[target-num] = i
