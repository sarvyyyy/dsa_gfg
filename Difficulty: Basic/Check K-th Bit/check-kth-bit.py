class Solution:
    def checkKthBit(self, n, k):
        ans = n & (1<<k)!=0
        return ans
        