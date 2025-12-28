# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        right = len(s)-1

        while left<right:
            if s[left].lower() == s[right].lower():
                left+=1
                right -=1
                continue
            else:
                return False
        return True