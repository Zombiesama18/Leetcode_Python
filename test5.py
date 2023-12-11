"""
/**
*
 * 把文本数据转换成文本型表格
 * 每条数据格式如line3 col1 A，表示第三行第一列的单元格的内容为A
 * 表格的行号、列号都从1开始
 * 内容为一个大写的英文字母，或者为空
 * 请将其转换为【文本型表格】，并输出：
 * 1.表格的行、列数分别为文本数据中的行、列的最大值。
 * 2.表格上下边框用字符+和-组成，+代表单元格的间隔，-代表一个字符的占位符
 * 3.表格的数据行：用字符|标志单元格的左右边界，单元格的宽度固定位3，内容非空时填中间，空时填入三个空格
 * 输入：
 * num表示文本数据的条数 num[1,20]
 * 其中行号[1,100]
 * 接下来num行字符
 *
 * 样例1：
    输入
    6
    line1 col2 A
    line1 col1 B
    line1 col3 C
    line2 col1 B
    line1 col4
    line1 col5 E
    输出
    +---+---+---+---+---+
    | B | A | C |   | E |
    | B |   |   |   |   |
    +---+---+---+---+---+
 * 样例2：
    输入
    2
    line1 col3
    line3 col2
    输出
    +---+---+---+
    |   |   |   |
    |   |   |   |
    |   |   |   |
    +---+---+---+

"""


n = int(input().strip())
data = []
for _ in range(n):
    temp = input().strip().split(' ')
    line = int(temp[0][4:])
    col = int(temp[1][3:])
    if len(temp) > 2:
        content = temp[2]
    else:
        content = ''
    data.append((line, col, content))
max_line = max([item[0] for item in data])
max_col = max([item[1] for item in data])
table = [['' for _ in range(max_col)] for _ in range(max_line)]
for line, col, content in data:
    table[line - 1][col - 1] = content
print('+---' * max_col + '+')
for i in range(max_line):
    for j in range(max_col):
        if table[i][j]:
            print(f'| {table[i][j]} ', end='')
        else:
            print('|   ', end='')
    print('|')
print('+---' * max_col + '+')

#
# if __name__ == '__main__':
#     func()
#


