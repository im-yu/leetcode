def calc(value):
    result = []
    while value:
        result.append(value % 10)
        value = value // 10
    #逆序，按正常的顺序返回
    result.reverse()
    return result
print(calc(123))


def method(value):
    #divmod()是内置函数，返回整商和余数组成的元组
    result = []
    while value:
        value, r = divmod(value, 10)
        result.append(r)
    result.reverse()
    return result
print(method(123))

def num2str(value):
    return list(map(int, str(value)))
print(num2str(123))

def ca(L:list):
    ans = 0
    for i in L:
        ans += i
    return ans
