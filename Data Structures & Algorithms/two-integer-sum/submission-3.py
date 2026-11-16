class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        s = {}

        for i in range(len(nums)):
            s[nums[i]] = i
        
        for i in range(len(nums)):
            if (target-nums[i] in s) and (i != s[target-nums[i]]):
                return [i, s[target-nums[i]]]

        
        