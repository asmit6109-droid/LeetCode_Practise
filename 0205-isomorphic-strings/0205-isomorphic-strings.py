class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping ={}
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            if a not in mapping:
                if b in mapping.values():
                    return False

            if a in mapping:
                if mapping[a] != b:
                    return False

            mapping[a] = b
        return True  