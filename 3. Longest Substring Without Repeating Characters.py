class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 1
        substring = ""
        max_len = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            substring = substring + s[left]
            while right < len(s):
                if s[right] not in substring:
                    substring = substring + s[right]
                    right = right + 1
                    print(substring)
                else:
                    left = left + 1
                    substring = substring[1:]
                max_len = max(len(substring), max_len)
            return max_len