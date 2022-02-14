# 399. 除法求值
# 给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。
# 输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
def calcEquation(equations, values, queries):
    all_possible = equations[:]
    for i in range(len(equations) - 1):
        for j in range(i + 1, len(equations)):
            if equations[i][1] == equations[j][0]:
                all_possible.append([equations[i][0], equations[j][1]])
                values.append(values[i] * values[j])
            if equations[i][0] == equations[j][0]:
                all_possible.append([equations[j][1], equations[i][1]])
                values.append(values[i] / values[j])
    temp = all_possible[:]
    for i in range(len(all_possible)):
        temp_list = all_possible[i][:]
        temp_list.reverse()
        temp.append(temp_list)
        values.append(1 / values[i])
    output = []
    for i in range(len(queries)):
        if queries[i] in temp:
            output.append(values[temp.index(queries[i])])
        else:
            output.append(-1.0)
    return output


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
calcEquation(equations, values, queries)
