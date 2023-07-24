class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if len(s) >= 1:
            l = [i for i in s.split(" ") if i != ""]
            print(l)
            return len(l)
        else:
            return 0
