class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(n^2) time #O(1) space
        res = []
        nums.sort()
        #index, value
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            #check if it previous 
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    #only move left
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                

            


            




