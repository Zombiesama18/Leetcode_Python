# 1002. 查找常用字符
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。


def commonChars(A):
    def recursion(comb, ind):
        if ind == len(A):
            return comb
        temp = []
        A[ind] = list(A[ind])
        for i in range(len(comb)):
            for j in range(len(A[ind])):
                if comb[i] == A[ind][j]:
                    temp.append(comb[i])
                    A[ind].remove(comb[i])
                    break
        return recursion(temp, ind + 1)

    return recursion(A[0], 1)


A = ["bella", "label", "roller"]
commonChars(A)
