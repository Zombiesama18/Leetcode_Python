# 68. 文本左右对齐
# 给定一个单词数组和一个长度   maxWidth，重新排版单词，使其成为每行恰好有   maxWidth   个字符，且左右两端对齐的文本。
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格   ' '   填充，使得每行恰好有 maxWidth   个字符。
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
# 说明:
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于   maxWidth。
# 输入单词数组 words   至少包含一个单词。
def fullJustify(words: [str], maxWidth: int) -> [str]:
    tempLength = 0
    wordLength = 0
    tempWords = []
    result = []
    for word in words:
        if tempLength + len(word) > maxWidth:
            if len(tempWords) == 1:
                result.append(''.join(tempWords[0]) + ' ' * (maxWidth - len(tempWords[0])))
            else:
                blanks = maxWidth - wordLength
                averageBlanks = blanks // (len(tempWords) - 1)
                extraBlanks = blanks % (len(tempWords) - 1)
                tempResult = ''
                while tempWords:
                    tempResult += tempWords.pop(0)
                    if tempWords:
                        tempResult += ' ' * (averageBlanks + 1) if extraBlanks > 0 else ' ' * averageBlanks
                        extraBlanks -= 1
                result.append(tempResult)
            tempWords = [word]
            tempLength = len(word) + 1
            wordLength = len(word)
        else:
            tempWords.append(word)
            tempLength += len(word) + 1
            wordLength += len(word)
    tempResult = ''
    while tempWords:
        tempResult += tempWords.pop(0)
        if tempWords:
            tempResult += ' '
        else:
            tempResult += ' ' * (maxWidth - len(tempResult))
    result.append(tempResult)
    return result


fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)



