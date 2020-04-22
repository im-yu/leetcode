# b = 5
# list1 = range(10)
# a = list1.index(b)
# print(b)
# print(list1[a])
# for i in list1[1:a]:
#     print(i)

# str = "abcdefg"
# str2 = ""
# print(str2.join(reversed(str)))
# print(list(reversed(str)))

# K = 3
# N = 4
# form = []
# print(form)
# Z = []
# for i in range(N+1):
#     Z.append(i)
# for i in range(K+1):
#     if i == 0:
#         form.append([0] * (N+1))
#     elif i == 1:
#         form.append(Z)
#     else:
#         form.append([])
#         for j in range(N+1):
#             if j == 0:
#                 form[i].append(0)
#             elif j == 1:
#                 form[i].append(1)
#             else:
#                 form[i].append(None)
#
# def Samlpe(i,j):
#     return max(drop(i,N-j),drop(i-1,N-1))
# def drop(i,j):
#     if form[i][j] == None:
#         tmp = []
#         while j == 0:
#             tmp.append(Samlpe(i,j))
#             j = j -1
#         form[i][j] = 1+min(tmp)
#     else:
#         return form[i][j]

# matrix = [[0,0,0],[0,1,0],[0,0,0]]
# m, n = len(matrix), len(matrix[0])
# zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 1]
# seen = set(zeroes_pos)
#
#
# print(zeroes_pos)
# print(seen)

# class UnionFind:
#     def __init__(self,grid):
#         m, n = len(grid), len(grid[0])
#         self.count = 0
#         self.parent = [-1] * (m * n)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     self.parent[i * n + j] = i * n + j
#                     self.count += 1
#     def find(self,i):
#         if self.parent[i] != i:
#             self.parent[i] = self.find(self.parent[i])
#         return self.parent[i]
#     def union(self,i,j):
#         p1 = self.find(i)
#         p2 = self.find(j)
#         if p1 != p2:
#             self.parent[p1] = p2
#             self.count -= 1
#     def getCount(self):
#         return self.count
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         nr = len(grid)
#         if nr == 0:
#             return 0
#         nc = len(grid[0])
#         uf = UnionFind(grid)
#         for r in range(nr):
#             for c in range(nc):
#                 if grid[r][c] == "1":
#                     grid[r][c] = "0"
#                     for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
#                         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
#                             uf.union(r * nc + c, x * nc + y)
#         return uf.getCount()

a = []
a[5] = 5
print(a)