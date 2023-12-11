# 692. 前K个高频单词
# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
def topKFrequent(words: [str], k: int) -> [str]:
    wordsDict = {}
    for word in words:
        if word not in wordsDict:
            wordsDict[word] = 1
        else:
            wordsDict[word] += 1
    wordListByFrequent = list(wordsDict.keys())
    wordListByFrequent.sort(key=lambda x: (-wordsDict[x], x))
    return wordListByFrequent[:k]


topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)

