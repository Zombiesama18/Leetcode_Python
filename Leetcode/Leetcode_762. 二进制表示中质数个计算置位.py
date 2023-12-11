"""
762. 二进制表示中质数个计算置位
给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。
计算置位位数 就是二进制表示中 1 的个数。
例如， 21 的二进制表示 10101 有 3 个计算置位。
"""


def countPrimeSetBits(left: int, right: int) -> int:
    def isPrime(number):
        if number == 1:
            return False
        temp = 2
        while temp * temp <= number:
            if number % temp == 0 and number // temp != 1:
                return False
            temp += 1
        return True

    primes = set()
    result = 0
    while left <= right:
        counter = bin(left).count('1')
        if counter in primes:
            result += 1
        else:
            if isPrime(counter):
                primes.add(counter)
                result += 1
        left += 1
    return result


countPrimeSetBits(6, 10)
