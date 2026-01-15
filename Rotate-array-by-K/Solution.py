# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def rotateAnArrayByK(self, nums,k):
        def rev(nums,l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l= l+1
                r= r-1
        k=k% len(nums)
        rev(nums,0,len(nums) -1)
        rev(nums,0,k-1)
        rev(nums,k,len(nums)-1)

        return nums

        
