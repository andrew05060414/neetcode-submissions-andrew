class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else: # 是反括号
                if not stack or stack[-1] != pairs[ch]: 
                # 栈是空的 or 栈顶那个左括号，和当前右括号，不是同一对
                    return False
                stack.pop()

        return len(stack) == 0