#Problem No. 20 - Valid Parenthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        pairs = {
        ')': '(',
        '}': '{',
        ']': '['}
        
        for i in s: 
            if i in '([{': #if any of these it will append, stack if fifo
                stack.append(i)
            else:
                if not stack or stack[-1] != pairs[i]:
                    return False
                
                stack.pop() #stack follows fifo
        return len(stack) == 0
# I learned about stack ----> FIFO 