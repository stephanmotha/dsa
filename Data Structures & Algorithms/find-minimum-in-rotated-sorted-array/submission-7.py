class Solution:
    def findMin(self, nums: List[int]) -> int:
        [4, 5, 1, 2, 3]
        [3, 1, 2]
        [3, 1]
        [1, 2, 3, 4]
        [4,5,6,7,0,1,2]
        [1, 2, 3]
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            # if in left sorted
            if nums[0] <= nums[mid]:
                l = mid + 1

            else:
                r = mid

        return nums[0]
        


        
        