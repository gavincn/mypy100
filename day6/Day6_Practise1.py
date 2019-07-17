"""
练习1：实现计算求最大公约数和最小公倍数的函数。
"""


# 最大公约数，能同时被两个数整除
def gcd(x, y):
    (x, y) = (y, x) if (x > y) else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


# 最小公倍数, 如4 和6 的最小公倍数是 12
# x 和 y 乘以某数后能得到的最小的相同的值
def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(4, 6))
print(lcm(4, 6))

"""
判断一个数是不是会问数的函数
"""


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


print(is_palindrome(151))

"""
判断一个数是不是素数
"""
from math import sqrt


def is_prime(num):
    tmp = int(sqrt(num))
    for i in range(2, tmp+1):
        if num % i == 0:
            return False
    return True

print()
print(is_prime(3))
print(is_prime(8))
print(is_prime(7))
print(is_prime(16))
print(is_prime(31))

if __name__ == "__main__":
    num = int(input("input a number please :"))
    if is_palindrome(num) and is_prime(num):
        print("%d是回文素数")


