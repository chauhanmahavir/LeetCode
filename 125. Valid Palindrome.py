class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_s = [i.lower() for i in s if i.isalnum()]
        final_s = "".join(final_s)
        return final_s == final_s[::-1]
