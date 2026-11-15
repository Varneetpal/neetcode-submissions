class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for letter in s:
            if not(letter.isalnum()):
                s = s.replace(letter, "")

        # Compare if the reverse and forward strings match
        r = s[::-1]

        if r == s:
            return True

        return False