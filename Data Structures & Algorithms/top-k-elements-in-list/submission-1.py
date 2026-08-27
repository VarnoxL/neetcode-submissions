import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        heap = []  # min-heap of (freq, num)
        for n, c in count.items():
            heapq.heappush(heap, (c, n))
            if len(heap) > k:
                heapq.heappop(heap)  # evict smallest freq

        return [n for c, n in heap]

        #o(nlogk) solution