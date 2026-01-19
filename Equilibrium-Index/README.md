Equilibrium Index
Level - Medium
Given an array of integers, find the equilibrium index where the sum of elements at lower indices is equal to the sum of elements at higher indices. Return the equilibrium index if it exists, otherwise return -1.

Examples:
Example 1:

Input: [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: In the input array, the sum of elements before index 3 is -1 (-7 + 1 + 5), and the sum of elements after index 3 is also -1 (-4 + 3). Hence, index 3 is the equilibrium index.

Example 2:
Input: [1, 2, 3, 4, 5]
Output: -1

Explanation: There is no equilibrium index in this input array as the sum of elements before and after any index is never equal.
Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
Time complexity: O(n)
Space complexity: O(1)
