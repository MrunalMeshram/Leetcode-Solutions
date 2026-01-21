# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def rearrangeArrayElementsBySign(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2
            else:
                res[neg] = num
                neg += 2

        return res
