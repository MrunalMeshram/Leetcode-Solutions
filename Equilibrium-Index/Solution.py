class Solution:
    def equilibriumIndex(self, nums: List[int]) -> List[int]:

        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - nums[i] - left
            if left==right:
                return i
            left += nums[i]
        return -1
