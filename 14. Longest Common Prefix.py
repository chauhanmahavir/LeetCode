class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for i in strs[0]:
            temp_prefix = common_prefix + i
            for j in strs:
                if j.startswith(temp_prefix):
                    continue
                else:
                    break
            else:
                common_prefix = temp_prefix
        return common_prefix
