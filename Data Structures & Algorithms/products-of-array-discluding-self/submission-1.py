class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        el = [1] * len(nums)
        er = [1] * len(nums)
        base = 1
        for i in range(len(nums)):
            el[i] = base
            base *= nums[i]

        base = 1
        result = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            er[i] = base
            base *= nums[i]
            result[i] = er[i]*el[i]

        # result = []
        # for i in range(len(nums)):
        #     result.append(el[i]*er[i])

        return result
        