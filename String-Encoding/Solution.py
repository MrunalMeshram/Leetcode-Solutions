# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def stringEncoding(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==")":
                temp=[]
                while stack[-1] != "(":
                    removed=stack.pop()

                    temp.append(removed)
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(i)    

        return "".join(stack)

