class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {} 
        for i, num in enumerate(nums): 
            pair = target - num
            if pair in dictionary:
                return [dictionary[pair], i]
            dictionary[num] = i
        return