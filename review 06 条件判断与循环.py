# 1 条件判断

# 1 if...else
a=10
if a>=10:
    print('a大于等于10')
else:
    print('a小于等于10')

# 2 if...elseif...else
age=22
if age >= 18:
    print('成年了')
elif age >= 16:
    print('半成年')
else:
    print('未成年')

# 2 循环
# 2.1 for 循环

username=['lisi','zhangsan','wanger']
for name in username:
    print(name)

# 2.2 while 循环

# 计算100以内所有奇数和
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

# 2.3 range()函数

# 遍历数列
for i in range(6):
    print(i)

# 指定范围，遍历
for i in range(4,8):
    print(i)

# 指定范围和步长
for i in range(2,9,2):
    print(i)