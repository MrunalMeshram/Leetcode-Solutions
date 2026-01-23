String Encoding
Medium
Acceptance: 33.6%
You are given a string s that consists of lower case English letters and brackets. Reverse the strings in each pair of matching parentheses, starting from the innermost one. Your result should not contain any brackets.

Examples:
Example 1:

Input:
(abcd)

Output:
dcba

Explanation:
The substring abcd is reversed to dcba.

Example 2:

Input:
(u(love)i)

Output:
iloveu

Explanation:
The substring u(love)i is reversed to ieloveu. The substring love is reversed to evol.

Example 3:

Input:
(ed(et(oc))el)

Output:
leetcode

Explanation:
The substring et(oc) is reversed to coet. The substring ed(coet)el is reversed to leetcode.

Constraints:
1 <= s.length <= 2000
s only contains lower case English letters and brackets
