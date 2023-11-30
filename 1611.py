class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        count = 0
        while n:
            count = - count - (n^(n-1))
            n &= n-1
        return abs(count)
        
