## python module and function

### function
function主要解决代码复用问题，可以将一段计算逻辑封装到一个称之为函数的功能模块中，
在需要此逻辑或计算的地方，只要调用这个函数即可。

#### definition of function
~~~python

def foo():
    #TODO your code

~~~
#### arguments of function
~~~python

def foo(param):

def foo(param1,param2):

def foo(param1 = 0,param2 = 0):

def foo(*params):
    for para in params:
        print(para)

~~~    

#### nested function
函数可以嵌套定义
~~~python

def foo():
    a = 100
    
    def bar():
        b = 200
        print(a+b)

~~~

### module

module，python中模块用来管理函数，比如将一类function封装在一个py文件中，
那这个py文件就是一个module，可以通过import modulexx来引用，或者通过from modulexxx import foo来引用其中的某个函数

#### __name__和__main__

当一个python文件执行的时候，如果没有默认执行的代码，则不会执行，
如果定义了 if __name__ == "__main__" : 的时候，则会执行if下的语句
但是这部分代码只会在当前py文件中有效，因为被import的时候__name__值为当前py文件的名字

如果module内，多个函数的名字相同，由于py中没有重载的概念，后面定义的函数会覆盖前面的函数。


### 作用于问题

python变量作用于主要用：
1. 全局作用域 **没有定义在任何一个函数中，所有函数都可以使用，除非函数中定义同名变量**
2. 局部作用域 **函数中定义的变量，在当前函数和内部嵌套函数中可以使用**
3. 嵌套作用域 **嵌套函数中定义的，外层函数也无法读取** 
4. 内置作用域 **python内置的那些隐含标志服，如min，len等**

### globle and nonlocal

参考varscope.py ， 就是在不通的作用域下强制修改制定的变量
如在funciton中修改全局变量，就要使用globle，
如在嵌套函数中修改上层变量，则使用nonlocal