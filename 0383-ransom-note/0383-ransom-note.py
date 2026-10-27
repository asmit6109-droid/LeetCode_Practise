class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for i in ransomNote:
            if i in count:
                count[i] -= 1
                if count[i] < 0:
                    return False
            else:
                return False
        return True
        