"""
2278. 字母在字符串中的百分比
给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。
"""


def percentageLetter(s: str, letter: str) -> int:
    return int(s.count(letter) / len(s) * 100)
