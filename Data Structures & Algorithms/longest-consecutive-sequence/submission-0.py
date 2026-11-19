class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            # start of sequence
            if num-1 not in s:
                local_lgst = 0
                temp = num
                while temp in s:
                    local_lgst += 1
                    temp+=1
                
                if local_lgst > ans:
                    ans = local_lgst

        return ans






        