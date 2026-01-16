# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def nonDecreasingArray(self, nums: List[int]) -> List[int]:
        
        count = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                    return False

                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]  # raise nums[i+1]
                else:
                    nums[i] = nums[i + 1]  # lower nums[i]

        return True

       
        
