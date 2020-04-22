class UnionFind:
    def __init__(self, M):
        m = len(M)
        self.count = 0
        self.parent = [-1] * (m)
        for i in range(m):
            self.parent[i] = i
            self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        p1 = self.find(i)
        p2 = self.find(j)
        if p1 != p2:
            self.parent[p1] = p2
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def findCircleNum(self, M) -> int:
        n = len(M)
        UF = UnionFind(M)
        for i in range(n):
            for j in range(i, n):
                if M[i][j] == 1 and i != j:
                    UF.union(i, j)
        return UF.getCount()
A = Solution()
M =[[[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],[[1,1,0],[1,1,0],[0,0,1]]]
for i in M:
    print(A.findCircleNum(i))

