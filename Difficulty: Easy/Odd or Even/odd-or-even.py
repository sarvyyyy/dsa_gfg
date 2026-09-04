class Solution:
    def isEven (self, n):
        if n&(1<<0):
            return False
        else:
            return True
        