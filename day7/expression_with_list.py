import sys


def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in "ABCD" for y in "123"]
    print(f)  # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3']
    # 用列表的生成表达式语句创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内容控件
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 10 :100  , 1000:4516
    print(f)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 请注意下面的代码创建的不是一个列表，而是一个生成器对象
    # 通过生成器可以获取到数据但它不赵勇额外的控件存储数据
    # 每次需要数据的时候就通过内部的运算得到数据（需要花费额外的时间）
    print()
    f = (x ** 2 for x in range(1, 100))
    print(sys.getsizeof(f))  # 64
    print(f)  # <generator object main.<locals>.<genexpr> at 0x011E8E30>
    # for val in f:
    #     print(val)

    # [x for x in range(1,10)] 为生成数据
    # (x for x in range(1,10)) 为数据生成器

    """
    定义列表 [xxx,xxx]
    定义元祖 (xxx,xxx)
    """
    t = ("罗庚", 38, True, "四川成都")
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError: 'tuple' object does not support item assignment
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 将元祖转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改他的元素的
    person[0] = "李小龙"
    person[1] = 25
    print(person)
    # 将列表转换成元祖
    t1 = tuple(person)
    print(t1)

"""
fib generate
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def genfib():
    for val in fib(10):
        print(val)


if __name__ == '__main__':
    main()
    # genfib()
