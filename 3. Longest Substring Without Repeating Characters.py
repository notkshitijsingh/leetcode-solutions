class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        distinct = []
        total = []
        i = 0
        while i < len(s):
            if s[i] not in distinct:
                if len(distinct) == 0:
                    start = i
                distinct.append(s[i])
                i += 1
            else:
                total.append(distinct)
                distinct = []
                i = start + 1
        total.append(distinct)
        ans = 0
        for sbs in total:
            if len(sbs) > ans:
                ans = len(sbs)

        return ans
