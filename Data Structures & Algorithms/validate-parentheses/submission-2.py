class Solution:
 def isValid(self, s: str) -> bool:
    stack = []
    close_to_open = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in close_to_open:          # it's a closing bracket
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()                # matched, remove the open bracket
            else:
                return False               # mismatch or nothing to match
        else:                              # it's an opening bracket
            stack.append(char)

    return not stack                       # valid only if nothing left over