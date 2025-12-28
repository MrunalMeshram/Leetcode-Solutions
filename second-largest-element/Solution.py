# Second Largest Element

# Given an integer array, find the second largest element in the array. You may assume the array contains at least two elements.

# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def secondLargestElement(self, nums: List[int], k: int) -> int:
        heap = []
        k=2
        for num in nums:
            heapq.heappush(heap,num)

            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
           
