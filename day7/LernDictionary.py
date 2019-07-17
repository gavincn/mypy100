"""
字典是领一种可变容器模型，类似于我们生活中使用的字典，它可以存储任意类型对象。
与里诶博爱，集合不通的是，字典的每个元素都是由一个key和value组成的键值对，
键和值通过冒号分开。
### 感觉跟json一样
"""


def main():
    scores = {"张三": 95, "李四": 78, "王五": 82}
    # 通过键获取字典中对应的值
    print(scores["张三"])
    print(scores["李四"])
    # 遍历
    for ele in scores:
        print("%s\t--->\t%d" % (ele, scores[ele]))
    scores["张三"] = 60
    scores["李四"] = 80
    scores.update(赵六=99, 田七=88)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))  # None
    # 如果武则天不存在则返回默认值60
    print(scores.get('武则天', 60))
    print(scores)

    # 删除字典中的元素
    print()
    print(scores)
    print(scores.pop("张三", 100))  # 如果存在，则返回字典值，否则返回默认的100
    print(scores.popitem())
    print(scores.popitem())
    print(scores)

    # 清空字典
    scores.clear()
    print(scores)
    

if __name__ == '__main__':
    main()
