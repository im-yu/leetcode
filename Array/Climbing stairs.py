class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        else:
            f1,f2,f3=1,2,3
        for i in range(3,n):
            f1 = f2
            f2 = f3
            f3 = f1 + f2
        return f3 
