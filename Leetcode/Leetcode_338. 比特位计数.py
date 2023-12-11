# 338. 比特位计数
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
def countBits_exhaustion(num):
    def count1(s):
        counter = 0
        for j in s:
            if j == '1':
                counter += 1
        return counter

    output = []
    for i in range(num + 1):
        number = bin(i)[2:]
        output.append(count1(number))
    return output


countBits_exhaustion(5)


def countBits_simple(num):
    result = list(range(num + 1))
    if num == 0:
        return result
    if num == 1:
        return result
    result[2] = 1
    if num == 2:
        return result
    for i in range(3, num + 1):
        if i % 2 == 0:
            result[i] = result[int(i / 2)]
        else:
            result[i] = result[int((i - 1) / 2)] + 1
    return result


countBits_simple(16)
