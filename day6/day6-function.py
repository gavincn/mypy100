"""
定义函数
在Python中可以使用def关键字来定义函数，和变量一样每个函数也有一个响亮的名字，
而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给函数的参数，
这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，
而函数执行完成后我们可以通过return关键字来返回一个值，这相当于数学上说的函数的因变量。
"""


def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = 5
n = 4
print(factorial(m) // factorial(n) // factorial(m - n))

from random import randint


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(a=50, b=100, c=200))


def addall(*args):
    total = 0
    for val in args:
        total += val
    return total


print(addall())
print(addall(1))
print(addall(1, 2, 3))
print(addall(1, 3, 5, 7, 9))

"""
用模块管理函数
对于任何一种编程语言来说，给变量、函数这样的标识符起名字都是一个让人头疼的问题，
因为我们会遇到命名冲突这种尴尬的情况。最简单的场景就是在同一个.py文件中定义了两个同名函数，
由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，
也就意味着两个函数同名函数实际上只有一个是存在的。
"""

def foo():
    print("hello,world!")

def foo():
    print("goodbye world!!!")

foo()



