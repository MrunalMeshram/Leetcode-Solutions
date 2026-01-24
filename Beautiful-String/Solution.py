from collections import Counter

class Solution:
    def isBeautiful(self, s: str) -> bool:
        count = Counter(s)

        prev = float('inf')  # very large number

        for ch in range(ord('a'), ord('z') + 1):
            curr = count.get(chr(ch), 0)
            if curr > prev:
                return False
            prev = curr

        return True
