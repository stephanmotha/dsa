class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10, 2, 3, 4, 5]
        # [1, 5, 2, 7, 1]
        # [5, 4, 3, 2, 1]
        # l = prices[0]
        # ans = -1
        # for i in prices:
        #     ans = max(ans, i-l)
        #     if i<l:
        #         l = i

        # return ans

        l = 0
        r = 0
        ans = -1
        while r<len(prices):
            ans = max(ans, prices[r]-prices[l])
            if prices[r]<prices[l]:
                l = r
            r += 1
        
        return ans



        