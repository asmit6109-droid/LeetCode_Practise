class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        for i in range(n):
            j = 0
            for k in range(i,n):
                if haystack[k] == needle[j]:
                    j += 1
                else:
                    break
                if j == m:
                    return i
        return -1

        