res = []
cur_s = ""
n = 3

def generate(level, max, cur_s):
    # terminator
    if level >= max:
        res.append(cur_s)
        return
    # process current
    # drill down
    generate(level + 1, max, cur_s + "(")
    generate(level + 1, max, cur_s + ")")


generate(0, 2 * n, cur_s)
print(res)