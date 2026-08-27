class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        eg: Input: nums = [1,2,2,3,3,3], k = 2
        Output: [2,3]
        """
        #use a hashmap for # of time value appear
        count = {}
        #intital freq list, +1 because it start at 0
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            #value n occur c amount of time 
            freq[c].append(n)
        
        ret = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret

