class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(char.lower() for char in s if char.isalnum())
        palindrome = s[::-1]
        if s == palindrome:
            return True
        return False
        

        # if s is the same with the reverse
        # return true
        # if its not a palindrome return false