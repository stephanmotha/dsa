from heapq import *
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = defaultdict(int)
        # for i in nums:
        #     d[i] += 1
        
        # heap = []

        # for key in d:
        #     heappush(heap, (d[key], key))
        #     if len(heap) > k:
        #         heappop(heap)

        # return [h[1] for h in heap]


        # d = defaultdict(int)
        # for i in nums:
        #     d[i] += 1
        # for key in d:
        #     heappush(heap, (-d[key], key))
        # result = []
        # for i in range(k):
        #     # print(heap)
        #     result.append(heappop(heap)[1])
        # return result


        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        freq = defaultdict(list)
        for val in d:
            freq[d[val]].append(val)

        result = []
        for i in range(len(nums), -1, -1):
            if i in freq:
                result += freq[i][0:k-len(result)]
            if len(result) == k:
                return result


        

        