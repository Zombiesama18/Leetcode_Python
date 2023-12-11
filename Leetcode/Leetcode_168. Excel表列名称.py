# 168. Excel表列名称
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 例如，
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
def convertToTitle(columnNumber: int) -> str:
    result = []
    while columnNumber > 0:
        columnNumber -= 1
        result.append(chr(ord('A') + columnNumber % 26))
        columnNumber //= 26
    return ''.join(result[::-1])


convertToTitle(28)
convertToTitle(701)
