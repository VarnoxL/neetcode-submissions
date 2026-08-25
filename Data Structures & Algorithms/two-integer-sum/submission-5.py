class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap
       #target - nums: then we look for if it exist
       seen = {}

       for i, j in enumerate(nums):
            if target - j in seen:
                return [seen[target - j], i]
            seen[j] = i

       

        