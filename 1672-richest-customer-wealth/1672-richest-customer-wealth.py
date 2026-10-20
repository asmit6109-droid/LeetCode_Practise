class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for i in range(0,len(accounts)):
            total = sum(accounts[i])
            if total > richest:
                richest = total
        return richest  