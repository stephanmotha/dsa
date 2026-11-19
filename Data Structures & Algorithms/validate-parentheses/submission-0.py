class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]":"["}

        # "[]"
        # "[()]"
        # "[{(})]"


        for b in s:
            if b in brackets:
                if not stack or brackets[b] != stack[-1]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(b)
        
        return len(stack) == 0
                
        