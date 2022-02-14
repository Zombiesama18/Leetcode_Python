# 273. 整数转换英文表示
# 将非负整数 num 转换为其对应的英文表示。
def numberToWords(num: int) -> str:
    singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
             "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    if num == 0:
        return 'Zero'

    def recursion(nums: int):
        s = ''
        if nums == 0:
            return s
        if nums < 10:
            s += singles[nums] + " "
        elif nums < 20:
            s += teens[nums - 10] + " "
        elif nums < 100:
            s += tens[nums // 10] + " " + recursion(nums % 10)
        else:
            s += singles[nums // 100] + ' Hundred ' + recursion(nums % 100)
        return s

    result = ''
    unit = int(1e9)
    for i in range(3, -1, -1):
        currentNum = num // unit
        if currentNum:
            num -= currentNum * unit
            result += recursion(currentNum) + thousands[i] + " "
        unit //= 1000
    return result.strip()

