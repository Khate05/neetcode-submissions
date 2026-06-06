class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        # Why zero? = because the index is 0 and its the staring
        right = len(nums) - 1
        # len(nums) - 1 the length of the list minus 1 to get the end index

        while left <= right: # checking if ascending order
            mid = left + (right - left) // 2 # find the middle

            if target == nums[mid]: # if the given target is equal to the middle return the middle index
                return mid

            elif target <  nums[mid]: # if target is less than the middle go check the right side
                right = mid - 1 

            else:
                left = mid + 1 # if not less than check the left side

        return -1 #if not on the list return -1 