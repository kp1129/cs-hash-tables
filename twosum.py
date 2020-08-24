"""
Given an array of integers, return INDICES of the two numbers such that they add up to a specific target.

You may assume that each input would have EXACTLY one solution, and you may not use the same element twice.

Example:

nums = [2, 7, 11, 15], target = 9
9 is the sum of 2 and 7, at indices 0 and 1
return [0, 1]
"""

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # if you need to map something that's not mapped for you, think dictionary

    index_mapping = {}

    # go through the sums
    # access to that number
    # target - number
    # if complement is in dict, return indices
    # else, put number in the dict

    for i in range(len(nums)):
        curr = nums[i]
        complement = target - curr
        # is my complement in dictionary?
        if complement in index_mapping:
            return [index_mapping[complement], i]
        else:
            index_mapping[curr] = i    