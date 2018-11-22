# -*_ coding: utf-8 -*-

# 调用函数
print(abs(100))
print(abs(-100))

print(max(1,2,3,6,-9))

# 数据类型转换
int('124')
int(23.2)
float('123.34')
str(1.234)
bool(1)

# 定义函数
def my_abs(x):
    #判断x是否是一个数
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

my_abs(-6)

def f(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

args=(1,2,3)
kw={'d':99,'x':'#'}
f(*args,**kw)

# 递归函数
def mfact(n):
    if n == 1:
        return 1
    return n * mfact(n-1)

print(mfact(10))