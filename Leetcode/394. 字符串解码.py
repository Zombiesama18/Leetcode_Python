# 394. 字符串解码
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
def decodeString(s):
    output = ''
    group = s.split(']')

    def recursion(temp):
        if temp == '':
            return ''
        if temp[0].isdigit():
            times = int(temp[0: temp.index('[')])
            subcomb = recursion(temp[temp.index('[') + 1:])
            return subcomb * times
        if temp[0].isalpha():
            if '[' in temp:
                word = temp[0: temp.index('[') - 1]
                return word + recursion(temp[temp.index('[') - 1:])
            else:
                return temp

    for i in group:
        output += recursion(i)
    return output


s = "2[abc]3[cd]ef"
decodeString(s)
