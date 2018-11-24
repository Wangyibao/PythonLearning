# 传入函数
def jia(x,y,f):
    return f(x)+f(y)

print(jia(1,-4,abs))

print('------------------------')
# map()
def f(x):
    return x*x

l=map(f,[1,3,5,7,9])
# 把iterator转换成list输出
print(list(l)) 

print('------------------------')
# reduce()
from functools import reduce
def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5]))
print('------------------------')
# filter()
def odd(n):
    return n%2==0

print(list(filter(odd,[1,2,3,4,5])))

print('------------------------')
# sorted
print(sorted([3,4,5,7,1,2]))
print(sorted([3,4,5,6,-38,34,2],key=abs,reverse=True))