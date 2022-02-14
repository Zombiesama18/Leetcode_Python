# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。


def groupAnagrams(strs):
    output = []
    history = []
    for i in strs:
        l = list(i)
        l.sort()
        if l not in history:
            history.append(l)
            output.append([])
            output[history.index(l)].append(i)
        else:
            output[history.index(l)].append(i)
    return output


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)
