class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        res = ''.join(char.lower() for char in s if char.isalnum())

        if (res != res[::-1]):
            return(False)
        else:
            return(True)
