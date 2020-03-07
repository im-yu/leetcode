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


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = (n + 1) * [0]

        def climb(i, n, memo):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = climb(i + 1, n, memo) + climb(i + 2, n, memo)
            return memo[i]

        return climb(0, n, memo)