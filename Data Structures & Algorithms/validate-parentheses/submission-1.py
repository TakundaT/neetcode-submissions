class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to the opening bracket it needs
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in pairs:
                # Closing bracket: the top of the stack must be its matching opener
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                # Opening bracket: push it and wait for its closer
                stack.append(c)

        # Valid only if every opener got closed
        return not stack