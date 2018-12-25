# 1 调用函数
# 调用绝对值的函数
abs(100)

abs(-100)

# 求最大值函数
max(1,2,3,5,6,-9)

# 1）数据类型转换
int('124')

int(23.12)

float('123.34')

str(1.234)

bool(1)

bool('')

bool(0)

# 2）给函数起个‘别名’：
a=abs # 变量a指向abs函数
a(-9) # 通过a调用abs函数

# 2 定义函数
# 定义一个函数
def my_func(x, y):
    # 执行语句
    return (x+y)

# 例：
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
# 1）空函数 
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

# pass可以用作占位符，在没想好写什么代码的时候，可以先放一个pass，让代码顺利运行起来。

# 2）参数检查

# 调用函数时，如果参数的个数不对，Python解释器会自动检查出来，并抛出 TypeError 异常。
# 当传入不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的 my_abs 函数没有写参数检查代码，会导致 if 语句出错，出错信息和 abs 函数的不一样。

# 修改 my_abs() 函数，对参数类型进行检查
def my_abs(x):
    if not isinstance(x,(int, float)): # 判断x是否是整型或浮点型
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

# 3 函数的参数
# 1）位置参数
def add(x,y): # 参数x和参数y时位置参数
    return x+y
# 2）默认参数
def add(x,y=2): # y是默认参数，为2
    return x+y

# 调用函数
add(5)  # 可以不写y参数的值，此时默认y为2带入
# 注意：
# 必选参数在前，默认参数在后
# 有多个默认参数时，调用时可以按照顺序提供默认参数，也可以不按顺序提供默认参数，此时需要把参数名写上。
def add_students(name, gender, age=18, city='nanjing'):
    return name,gender,age,city

# 调用，按顺序
add_students('lisi','M',7) # age为7，city为默认的值
add_students('wanger','M', city='shanghai') # age为默认值，city为shanghai

# 3）可变参数
# 定义一个函数，计算平方和
def calc(*numbers): # 可变参数就是在普通参数前面加*
    sum=0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用函数
calc(1,2) # 结果是5
calc() # 结果是0

# 4）关键字参数
# 定义一个含关键字参数的方法
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

# 调用方法，传入必要参数
person('lisi',30)
# name:  lisi age:  30 other:  {}
# 调用方法，传入关键字参数
person('zhangsan',34,city='nanjing')
# name:  zhangsan age:  34 other:  {'city': 'nanjing'}
# 调用方法，传入一个dict
ex={'city':'shanghai','sex':'F'}
person('wanger',23,**ex)
# name:  wanger age:  23 other:  {'city': 'shanghai', 'sex': 'F'}

# 5）命名关键字参数

# 如果要限制关键字参数的名字，可以用命名关键字参数。
# 定义方法，带有命名关键字参数
def user(name,age,*,sex,city):
    print(name,'\t',age,'\t',sex,'\t',city)

# 调用方法，传入命名关键字参数，此参数名要和方法定义中的相同
user('lisi',23,sex='f',city='nanjing')

# 调用方法，传入的命名关键字参数的名字与定义时不同，出错！
user('zhangsan',22,sexx='m',ci='beijing')

# 6）参数组合 
# 在Python定义函数中，可以有多种类型参数组合。 
# 参数定义的顺序是： 
# 必选参数、默认参数、可变参数、命名关键字参数、关键字参数

# 4 递归函数
# 在函数内部，可以调用其他函数，如果在一个函数在内部调用自己本身，这个函数就是递归函数。

# 示例：算阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# 1）尾递归

# 解决递归调用栈溢出的方法时通过尾递归优化。

# 尾递归是指，在函数返回的时候，调用自身本身，并且return语句不能包含表达式。这样，编译器或解释器可以把尾递归做优化，无论递归调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 示例：将上面求阶乘函数改成尾递归方式

def fact(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)