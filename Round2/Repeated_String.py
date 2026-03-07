# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false
# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.

from collections import defaultdict
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(1, len(s)//2 + 1):
            if n % i ==0:
                if s[:i] * (n // i) == s:
                    return True
        return False
                