class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, nums in enumerate(nums):
            pair = target - nums
            if  pair in dictionary:
                return [dictionary[pair], i]
            dictionary[nums] = i
        return
