class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_count = 0
        for el in s:
            if el == "(":
                stack.append(el)
                if len(stack) > max_count:
                    max_count = len(stack)
            elif el == ")":
                stack.pop()
        return max_count