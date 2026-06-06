class Solution:
    def isValid(self, s: str) -> bool:

        brackets = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in "([{":
                brackets.append(char)
            else:
                if not brackets or brackets.pop() != pairs[char]:
                    return False
        return not brackets
            
        