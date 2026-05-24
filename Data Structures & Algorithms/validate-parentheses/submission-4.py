class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ")" and stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "}" and stack:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif i == "]" and stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0
