class Solution:
    def longestPalindrome(self, s: str) -> str:
        final_str = ""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                sub_str = s[i:j]
                if sub_str == sub_str[::-1] and len(sub_str) > len(final_str):
                    final_str = sub_str
        return final_str