Rearrange Array Elements By Sign
Medium

Given an integer array nums of 2n elements with an equal number of positive and negative elements, rearrange the elements in the array such that the modified array follows the conditions:

- Every consecutive pair of elements have opposite signs.

- For all integers with the same sign, the order in which they were present in nums is preserved.

Return the modified array after rearranging the elements to satisfy the above conditions.

Examples:
Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation: The positive numbers are [3,1,2] and the negative numbers are [-2,-5,-4]. The output array alternates positive and negative numbers while preserving the original order within each sign.
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation: The positive number is [1] and the negative number is [-1]. The output alternates positive and negative numbers.
Example 3:

Input: nums = [1,-1,2,-2,3,-3]
Output: [1,-1,2,-2,3,-3]
Explanation: The input already satisfies the condition of alternating signs and preserving order.
Constraints:
2 <= nums.length <= 2 * 10^5
nums.length is even
1 <= |nums[i]| <= 10^5
nums contains equal number of positive and negative integers
