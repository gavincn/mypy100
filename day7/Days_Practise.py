"""
练习1：在屏幕上显示跑马灯文字
"""

import os
import time
import random


def practise1():
    content = "北京欢迎你，为你开天辟地......"
    while True:
        os.system("cls")
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code(code_len=4):
    """
    :param
    :param code_len:验证码长度
    :return:
    """
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename:文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """

    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""


"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值
"""


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    print(m1, m2)  # 12 5
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def main():
    # practise1()
    code = generate_code(8)
    print(code)
    suffix = get_suffix("abc.txt")
    print(suffix)
    a, b = max2([5, 12, 4, 6, 8, 9, 7, 5, 4])
    print(a, b)


if __name__ == '__main__':
    main()
