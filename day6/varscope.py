"""
Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索，
前三者我们在上面的代码中已经看到了，
所谓的“内置作用域”就是Python内置的那些隐含标识符min、len等都属于内置作用域）
"""

def foo():
    b = "hello"

    def bar():
        c = True
        print(a, "in bar")
        #print(b, "in bar") # 使用了nonlocal，就不能咋嵌套函数中重新定义b了
        #nonlocal b #加上这句，b改的就是外层的局部变量 ，不加下面的b是bar函数的局部变量，与foo的b无关
        b = "hello world"
        print(b, "in bar after nonlocal")
        print(c, "in bar")

    bar()
    print(b , "in foo after bar()")
    # print(c)#NameError: name 'c' is not defined


"""
同样的a变量，在fuu中覆盖了全局变量，同样 main中也获取不到fuu中的a
"""

def fuu():
    # 使用了global后， 程序最后打出的a就是全局变量  200 in main
    # 否则是 100 in main
    global  a
    a = 200
    print(a, "in fuu")
    #global  a
    print(a , " global a in fuu")
    #nonlocal a
    print(a , "nonlocal a in fuu")



if __name__ == "__main__":
    a = 100
    # cant print b here
    foo()
    fuu()
    print(a, "in main")
