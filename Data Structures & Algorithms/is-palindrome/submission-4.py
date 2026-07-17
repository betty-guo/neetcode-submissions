# input: string s
# output: bool true if it is a palindrome, otherwise false
# palindroms is same forward and backwards
# case insensitive, ignores non alphanumeric characters
# e.g. ignore spaces, and other characters. always convert to lower case
class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s)-1
        while L < R:
            if not s[L].isalnum(): # need to skip non alphanumeric characters
                L += 1
                continue
            elif not s[R].isalnum():
                R -= 1
                continue
            elif s[L].lower() != s[R].lower(): # need to convert to lowercase
                return False
            L += 1
            R -=1
        return True
