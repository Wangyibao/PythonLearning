# -*_ coding: utf-8 -*-

# 切片
arr=['zhangsan','lisi','wanger']
print(arr[0:2])
print(arr[:2])

print(arr[-1:])
print(arr[-2:])

ll=list(range(50))

print(ll[:12:2])
print(ll[::6])

print('----------------------------------------------------------')
# 迭代
grade_map={'lisi':99,'zhangsan':94,'wanger':100}
for key in grade_map:
    print(key)
print('----------------------------------------------------------')
for value in grade_map.values():
    print(value)
print('----------------------------------------------------------')
for k,v in grade_map.items():
    print(k,':',v)
print('----------------------------------------------------------')
from collections import Iterable
print(isinstance(grade_map,Iterable))
# 实现下标循环
for i,value in enumerate(['a','b',1]):
    print(i,value)
print('----------------------------------------------------------')
for x,y in [(1,1),(2,4),(2,7)]:
    print(x,y)
print('----------------------------------------------------------')
# 列表生成式
l=list(range(1,11))
print(l)
ll=[x*x for x in range(1,11) if x%2==0]
print(ll)
ll2=[m+n for m in 'abc' for n in 'xyz']
print(ll2)
ll3=[k+'='+str(v) for k,v in grade_map.items()]
print(ll3)