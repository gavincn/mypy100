def foo():
    pass

def bar():
    pass


"""
__name__ 是python中一个隐含的变量，他代表了模块的名字
只有被python解释器直接执行的模块的名字才是__main__
如果是别别的py引用，__name__的值是module3 ，py文件的名字
写main的好处是
"""

if __name__ == "__main__":
    print("call foo()")
    foo()
    print("call bar()")
    bar()

print("out if")
print("call foo()")
foo()
print("call bar()")
bar()
