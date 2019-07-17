"""
sum 1~100
range(101) generate a list from 0 to 100
range((1,100) 1-99
range(1,100,2) 1-99 的技术 2为步长
"""

sum = 0
for x in range(1, 101):
    sum += x
print(sum)

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

sum = 0
for x in range(1, 101, 2):
    sum += x
print(sum)

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)

"""
猜数小游戏
随机生成一个数字，每次输入自己猜测的数字，程序给予提示直到才对。
"""

import random

answer = 10  # 10random.randint(1, 100)
counter = 0
while True:
    counter += 1;
    number = 10  # int(input("请输入:"))
    if number < answer:
        print("大一点")
    elif number > answer:
        print("小一点")
    else:
        print("恭喜你猜对了")
        break;
print("你共猜了%d次" % counter)
if (counter > 7):
    print("您的智商余额不足!")

"""
99乘法表
"""

for x in range(1, 10):
    for y in range(1, x + 1):
        print("%d * %d = %d" % (x, y, x * y), end="\t")
    print()

"""
practice 1
检查素数
"""

from math import sqrt

num = 13
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("%d is prime" % num)
else:
    print("%d is not prime" % num)

"""
计算最大公约数和最小公约数
"""

x = 6
y = 100

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是:%d" % (x, y, factor))
        print("%d和%d的最小公约数是:%d" % (x, y, x * y // factor))
        break

"""
打印三角图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

num = 5;
for x in range(num):
    for y in range(x + 1):
        print("*", end="")
    print()

for x in range(num, 0, -1):
    for y in range(x - 1):
        print("", end=" ")
    for z in range(num - x + 1):
        print("*", end="")
    print()

for x in range(1, num+1):
    for y in range(num - x):
        print("", end=" ")
    for z in range(2 * x - 1):
        print("*", end="")
    print()

row = 5
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()