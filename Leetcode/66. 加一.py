# 66. 加一
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
def plusOne(digits: [int]) -> [int]:
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        number = digits[i] + carry
        if number == 10:
            digits[i] = 0
        else:
            digits[i] = number
            break
        if i == 0:
            digits.insert(0, 1)
    return digits


plusOne([1,2,9])
plusOne([9,9,9,9])
plusOne([0])


