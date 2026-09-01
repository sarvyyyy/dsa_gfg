class Solution:
    def checkSubsequenceSum(self, arr, k):
        possible = {0}
        
        for num in arr:
            new = set(possible)
            for i in possible:
                if i+num <= k:
                    new.add(i+num)
            possible = new
            
        return k in possible