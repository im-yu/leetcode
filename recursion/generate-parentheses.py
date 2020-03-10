# res = []
# cur_s = ""
# n = 3
#
# def generate(level, max, cur_s):
#     # terminator
#     if level >= max:
#         res.append(cur_s)
#         return
#     generate(level + 1, max, cur_s + "(")
#     generate(level + 1, max, cur_s + ")")
# generate(0, 2 * n, cur_s)
# print(res)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res =[]
        cur_s = ""
        def generate(left, right, nmax, cur_s):
            if right == nmax and left == nmax:
                res.append(cur_s)
                return
            if left < nmax:
                generate(left+1,right,nmax,cur_s+"(")
            if left > right:
                generate(left,right+1,nmax,cur_s+")")
        generate(0,0,n,cur_s)
        return res