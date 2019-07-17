"""
常用数据结构，列表，元祖，集合和字典
"""


def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)  # [1, 3, 5, 7, 100]
    list2 = ["hello"] * 5  # ['hello', 'hello', 'hello', 'hello', 'hello']
    print(list2)  # 5
    # 计算列表长度
    print(len(list1))  # 5
    # 使用下标
    print(list1[0])  # 1
    print(list1[4])  # 100
    # print(list1[5]) # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]

    # append element
    list1.append(200)
    list1.insert(1, 400)
    list1.insert(0, 500)
    list1 += [1000, 2000]
    print(list1)  # [500, 1, 400, 3, 300, 7, 100, 200, 1000, 2000]
    print(len(list1))  # 10

    # remove element
    list1.remove(400)
    print(list1)  # [500, 1, 3, 300, 7, 100, 200, 1000, 2000]
    print(len(list1))  # 9

    if 100 in list1:
        list1.remove(100)
    print(list1)  # [500, 1, 3, 300, 7, 200, 1000, 2000]

    # 使用下标删除
    del list1[0]
    print(list1)  # [1, 3, 300, 7, 200, 1000, 2000]

    # 清空列表元素
    list1.clear()
    print(list1)  # []

    """
    列表切片
    """
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    print(fruits)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=" ")  # Grape Apple Strawberry Waxberry Pitaya Pear Mango
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # ['apple', 'strawberry', 'waxberry']
    # fruits3 = fruits # 没有复制列表，只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)  # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)  # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']

    """
    列表排序
    """
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    print(list2)  # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
    print(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    print(list3)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print()
    print(list1)
    print(list2)
    print(list3)
    print(list4)

    # 给列表对象发出排序消息直接在列表对象上进行排序
    print()
    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()
