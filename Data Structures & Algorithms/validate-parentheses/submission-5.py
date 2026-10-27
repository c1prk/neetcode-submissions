class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c=0
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                c+=1
            elif len(stack)!=0:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                elif stack[-1] == '{' and i == '}':
                    stack.pop()
                elif stack[-1] == '[' and i == ']':
                    stack.pop()
        return not stack and c*2==len(s)