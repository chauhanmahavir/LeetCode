class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)
        vowels = "aeiouAEIOU"
        final_string = ""
        vowel_list = []

        for i in s:
            if i in vowels:
                vowel_list.append(i)
        vowel_list = vowel_list[::-1]
        for i, v in enumerate(s):
            if v in vowels:
                final_string = final_string + vowel_list[0]
                del vowel_list[0]
            else:
                final_string = final_string + s[i]
        return final_string
