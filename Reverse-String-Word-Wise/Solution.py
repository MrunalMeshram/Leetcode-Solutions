# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def reverseStringWordWise(self, s: str) -> str:
        word=s.split()
        word.reverse()
        return " ".join(word)
