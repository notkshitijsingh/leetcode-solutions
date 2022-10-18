class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        start = 0
        length = len(s)
        low = 0
        high = 0

        for i in range(1, length):
            low = i - 1
            high = i
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1

            low = i - 1
            high = i + 1
            while low >= 0 and high < length and s[low] == s[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1

        return s[start:start + max_length]
