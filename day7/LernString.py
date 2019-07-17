"""
字符串，由零个或多个字符组成的有限序列
"""


def main():
    str1 = "hello, world!"
    # 通过len函数计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello , workld
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO , WORKLD
    # 从字符串中查找子串所在位置
    print(str1.find("or"))  # 8
    print(str1.find("shit"))  # -1
    # 与find类似但找不到子串时会引发异常
    print(str1.index("or"))  # 8
    # print(str1.index("shit"))  # ValueError: substring not found
    # 检查字符串是否以制定的字符串开始
    print(str1.startswith("he"))  # True
    print(str1.startswith("He"))  # False
    # 检查字符串是否以制定的字符串结尾
    print(str1.endswith("d!"))  # True
    #  将字符串以制定的宽度居中并在两侧填充制定的字符
    print(str1.center(50, "*"))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))

    str2 = 'abc123456'
    # 从字符串中取出制定位置的字符（下标运算
    print(str2[2])  # c
    # 字符串切片（从指定位置开始到制定位置结束
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    # 两个冒号  从第一位开始：：步长
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba

    print(str2[-3:-1])  # 45

    print(str2[-3::-1])  # 4321cba
    print(str2[-3::2])  # 46

    # 检查字符串是否有数字构成
    print(str2.isdecimal())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # Fasle
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True

    # 去量表空格
    str3 = "    liu_shubin@163.com   "
    print(str3.strip())  # liu_shubin@163.com


if __name__ == '__main__':
    main()
