class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TARGET 1
        # [3, 4, 5, 6, 1, 2]
        # [1, 2, 3, 4, 5]
        # [4, 5, 1, 2, 3]
        # [2, 3, 4, 5, 1]
        # [5, 1, 3]


        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l+r)//2
            print(mid)
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1

                else:
                    l = mid + 1

            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return -1





            

        return -1

            
  

            








        