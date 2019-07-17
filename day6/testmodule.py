
from module1 import foo

foo()

from module2 import foo

foo()

import module1 as m1
import module2 as m2

m1.foo()

m2.foo()

print()
# 但是如果将代码写成了下面的样子，
# 那么程序中调用的是最后导入的那个foo，因为后导入的foo覆盖了之前导入的foo。

from module1 import foo
from module2 import foo

# 输出goodbye, world!
foo()

from module2 import foo
from module1 import foo

# 输出goodbye, world!
foo()

import module3