# 187. 重复的DNA序列
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
def findRepeatedDnaSequences(s: str) -> [str]:
    if len(s) <= 10:
        return False
    sequenceSet = set()
    resultSet = set()
    initialSequence = []
    initialSequence.extend(s[:10])
    sequenceSet.add(s[:10])
    for i in range(10, len(s)):
        initialSequence.pop(0)
        initialSequence.append(s[i])
        tempSequence = ''.join(initialSequence)
        if tempSequence not in sequenceSet:
            sequenceSet.add(tempSequence)
        else:
            resultSet.add(tempSequence)
    return list(resultSet)



