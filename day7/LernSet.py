"""
Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。

"""


def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)  # {1, 2, 3}
    print("length:", len(set1))  # length: 3
    set1.add(4)
    set1.add(5)
    print(set1)  # {1, 2, 3, 4, 5}
    print()
    set2 = set(range(1, 10))
    print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set2.update([11, 12])
    print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    set2.discard(5)  # remove value from set
    print(set2)  # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}
    if 4 in set2:
        set2.remove(4)
    print(set2)  # {1, 2, 3, 6, 7, 8, 9, 11, 12}
    print()

    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')  # 1 4 9 36 49 64 81 121 144

    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())  # 1
    print(set3)  # {2, 3}
    print(set1, set2)  # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12}

    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)  # {1, 2, 3}
    # print(set.intersection(set2)
    print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    print(set1 - set2)  # {4, 5}
    print(set1.difference(set2))  # {4, 5}
    print(set1 ^ set2)  # {4, 5, 6, 7, 8, 9, 11, 12}
    print(set1.symmetric_difference(set2))  # {4, 5, 6, 7, 8, 9, 11, 12}

    # 判断子集和超集
    print()
    print(set1, set2, set3)  # {1, 2, 3, 4, 5} {1, 2, 3, 6, 7, 8, 9, 11, 12} {2, 3}
    print(set2 <= set1)  # False
    print(set2.issubset(set1))  # False
    print(set3 <= set1)  # True
    print(set3.issubset(set1))  # True
    print(set1 >= set2)  # False
    print(set1.issuperset(set2))  # False
    print(set1 >= set3)  # True
    print(set1.issuperset(set3))  # True


if __name__ == '__main__':
    main()
