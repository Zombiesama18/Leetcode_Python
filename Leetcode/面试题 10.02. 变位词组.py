# 面试题 10.02. 变位词组
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
def groupAnagrams(strs: [str]) -> [[str]]:
    groupDict = {}
    result = []
    counter = 0
    for string in strs:
        tempString = ''.join(sorted(string))
        if tempString not in groupDict:
            groupDict[tempString] = counter
            counter += 1
            result.append([string])
        else:
            result[groupDict[tempString]].append(string)
    return result


groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])



