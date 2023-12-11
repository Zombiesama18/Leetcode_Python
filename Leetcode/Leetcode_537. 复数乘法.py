"""
537. 复数乘法
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
实部 是一个整数，取值范围是 [-100, 100]
虚部 也是一个整数，取值范围是 [-100, 100]
i2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
"""


def complexNumberMultiply(num1: str, num2: str) -> str:
    num1_real, num1_img = num1.split('+')
    num1_img = num1_img.split('i')[0]
    num2_real, num2_img = num2.split('+')
    num2_img = num2_img.split('i')[0]
    result_real = int(num1_real) * int(num2_real) - int(num1_img) * int(num2_img)
    result_img = int(num1_real) * int(num2_img) + int(num1_img) * int(num2_real)
    return f'{result_real}+{result_img}i'

