class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mulpt = 1
        r_mulpt = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1
            l_arr[i] = l_mulpt
            r_arr[j] = r_mulpt
            l_mulpt *= nums[i]
            r_mulpt *= nums[j]

        return[l * r for l, r in zip(l_arr, r_arr)]
