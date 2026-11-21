class Solution:
    def findMin(self, nums: List[int]) -> int:
        [4, 5, 1, 2, 3]
        [3, 1, 2]
        [3, 1]
        [1, 2, 3, 4]
        [4,5,6,7,0,1,2]
        if len(nums) == 1:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            print(mid)
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]

            # if in left sorted
            if nums[0] <= nums[mid]:
                print("here1")
                l = mid + 1

            else:
                print("here2")
                r = mid

        return nums[0]
        


        
        