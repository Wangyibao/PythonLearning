'''
1 生成器
产生背景：
    列表的容量有限
    如果创建了一个容量很大的列表，然而只需要访问前面几个元素，则有许多空间被浪费
    如果列表元素可以按照某种算法推算出来，在可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list，从而节省大量空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

1）创建generator

generator是使用 ( )，List是使用 [ ]。
'''
# 创建一个List
L=[x * x for x in range(10)]


# 创建一个generator
g=(x * x for x in range(10))


# 使用next()函数返回generator的下一个返回值
next(g)

next(g)

next(g)

next(g)


# 在没用更多的元素时，会抛出StopIteration的错误提示

# 使用for循环迭代generator
for n in g:
    print(n)

# 2）求斐波那契数列
# 定义普通函数
def fib(num):
    n,a,b=0,0,1
    while n < num:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

# 改进上面的函数，使用generator
def fib_g(num):
    n,a,b=0,0,1
    while n < num:
        yield b 
        a,b=b,a+b
        n=n+1
    return 'done'
# 如果一个函数定义中包含了yield关键字，则此函数是一个generator，而并非一个普通函数

# 运行结果 
fib_g(6)

for n in fib_g(6):
    print(n)

# 3）generator执行流程（顺序）
# 1. 定义一个generator
def see():
    print('step1')
    yield 1
    print('step2')
    yield (3)
    print('step3')
    yield(5,)

# 运行
s=see() # 创建一个generator对象
next(s)

next(s)

next(s)

'''
2 迭代器
    可以直接作用于for循环的对象统称为可迭代对象：Iterable
    可以被 next() 函数调用并不断返回下一个值的对象称为迭代器：Iterator
    list、dict、str是Iterable，不是Iterator，但是它们可以变成Iterator。
'''
from collections import Iterator
# 使用iter()函数，将list变为了Iterator 
isinstance(iter(['lisi','wanger']),Iterator)
