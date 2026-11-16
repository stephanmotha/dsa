from heapq import *
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        heap = []
        for key in d:
            heappush(heap, (-d[key], key))

        result = []
        for i in range(k):
            # print(heap)
            result.append(heappop(heap)[1])

        return result
        

        