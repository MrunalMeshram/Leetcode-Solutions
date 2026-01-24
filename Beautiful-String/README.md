Beautiful Strings
Easy
Acceptance: 55.9%
A string is considered beautiful if it satisfies the following conditions: Each letter in the string appears at most as many times as the previous letter in the alphabet; i.e. b occurs no more times than a; c occurs no more times than b; etc. Given a string, check whether it is beautiful.

Examples:
Example 1:

Input:
aab

Output:
true

Explanation:
In this case, 'a' occurs 2 times, 'b' occurs 1 time, and no other letter occurs, so it is a beautiful string.

Example 2:

Input:
aabbb

Output:
false

Explanation:
In this case, 'a' occurs 2 times, 'b' occurs 3 times, violating the condition, so it is not a beautiful string.

Example 3:

Input:
bbc

Output:
true

Explanation:
In this case, 'b' occurs 2 times, 'c' occurs 1 time, and no other letter occurs, so it is a beautiful string.

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters
