# -*_ coding: utf-8 -*-

# 判断
a=22
if a>=18:
    print('成年了')
elif a>=16:
    print('半成年')
else:
    print('未成年')

print("---------------------------------------------------------")

# for循环
username=['zhangsan','lisi','wanger']
for name in username:
    print(name)

# while
msum=0
n=99
while n>0:
    msum=msum+n
    n=n-2
print(msum)

# range()函数
for i in range(6):
    print(i,end="")

print()
for i in range(4,8):
    print(i,end="")

print()
for i in range(1,10,2):
    print(i,end="")