"""
寻找水仙花数
153 : 1^3 + 5^3 + 3^3 = 153
"""

from math import pow

num = int(500)

for i in range(2, num + 1):
    strNum = str(i)
    sum = 0;
    for s in strNum:
        sum += pow(int(s), 3)
    if (sum == i):
        print("%d 是 水仙花" % i)

    # if sum(s for s in strNum) : pow(int(s), 3) == i:
    #    print("%d 是 水仙花" % i)

"""
寻找完美数
如6，约束为1,2,3,4，出去6本身，其余3个数相加为：1+2+3=6
如28， 1,2,4,7,14,28,1+2+4+7+14=28
"""

for i in range(1, 100):
    sum = 0;
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print("%d is a perfect number" % i)

    # if sum([a for a in range(1, i) if i % a == 0]) == i:
    #    print("%d is a perfect number" % i)

"""
百鸡百钱 ：
我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""

x = 5
y = 3
# z = float(1 / 3)
cash = 100

for i in range(cash // x):
    for j in range(cash // y):
        # if i * 5 + j * 3 + k * z == 100 and i + j + k == 100:
        # k = 100-i-j
        if (100 - i * 5 - j * 3) * 3 == 100 - i - j:
            print("可以买%d只公鸡，%d只母鸡，%d只鸡雏" % (i, j, 100 - i - j))

"""
斐波那契数列
"""
fib = 0
theLast = 1
for i in range(10):
    """
    if i == 1:
        tmp = 3
  
    tmp = 2 : 卢卡斯数列L(n) 1 3 4 7 11 18 29 47 76 123 
    tmp = 3 : 1 4 5 9 14 23 37 60 97 157 
    """
    last = theLast
    # next last
    theLast = fib
    fib += last
    print(fib, end=" ")
print()
"""
Craps赌博游戏：
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""
from random import randint

money = 1000
while money > 0:
    bet = int(input("还剩：%d ,玩家掷骰子！请输入赌注:" % money))
    diceTotal1 = randint(1, 6) + randint(1, 6)
    print("骰子：", diceTotal1)
    if diceTotal1 == (7 or 11):
        print("玩家胜")
        money += bet
    elif diceTotal1 == (2 or 3 or 12):
        print("庄家胜")
        money -= bet
    else:
        diceTotal2 = randint(1, 6) + randint(1, 6)
        print("骰子：", diceTotal1)
        if diceTotal2 == 7:
            print("庄家胜")
            money -= bet
        elif diceTotal2 == diceTotal1:
            print("玩家胜")
            money += bet
        else:
            print("庄家胜")
            money -= bet
    print("再来一局吧！")
print("钱输光了！！！")
