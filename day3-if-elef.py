import getpass

username = "liu"
password = "wpd"

# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')

if username == "liu" and password == "pwd":
    print("successful")
else:
    print("login fail!")

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

"""
x = 10  # float(input("input a number = "))

if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))

"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)

flat is better than nested , so the code up is better
"""

if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3

print("f(%.2f) = %.2f" % (x, y))

"""
英制单位英寸和公制单位厘米互换
"""
value = 10  # float(input("please input length:"))
unit = 'in'  # input("please input unit:")

if (unit == "in"):
    print("%.2f in = %.2f cm" % (value, value * 2.54))
elif (unit == "cm"):
    print("%.2fcm = %.2fin" % (value, value / 2.54))
else:
    print("input wrone!")

"""
roll dice
"""
from random import randint

face = randint(1, 6)
print(face)
if (face == 1):
    print("you throw one")
elif face == 2:
    print("you throw two")
elif face == 3:
    print("you throw three")
elif face == 4:
    print("you throw four")
elif face == 5:
    print("you throw five")
elif face == 6:
    print("you throw six")

score = 20  # float(input("please input the score"))

if score >= 90:
    print("you got A")
elif score >= 80:
    print("you got B")
elif score >= 70:
    print("you got C")
elif score >= 60:
    print("you got D")
else:
    print("you got E")

"""
calc 三角形周长
"""
import math

a = 2
b = 2
c = 3
if a + b > c and b + c > a and a + c > b:
    print("周长=%.2f" % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("面积=%.2f" % (area))
else:
    print("不是三角形")

"""
计算五险一金
"""
salary = 22000.00
insurance = 2000.00
diff = salary - insurance - 3500

if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 5505

tax = abs(diff * rate - deduction)
print("个人所得税:%.2f元" % tax)
print("实际到手收入: %.2f元" % (diff + 3500 - tax))
