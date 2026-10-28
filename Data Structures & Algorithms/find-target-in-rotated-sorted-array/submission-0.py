"""
eg:Input: nums = [3,4,5,6,1,2], target = 1

Output: 4

brute force:
loop through every elements for target

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:   
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            #left half sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            #right half sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
