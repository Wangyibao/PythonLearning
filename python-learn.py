# -*_ coding: utf-8 -*-

# day01
# 输出
print('hello world');
print('hello','world','hello','python');
print(300);
print(100+300);
print('100+200= ',100+200);

# 输入
# name=input(); # 输入任意字符，按回车完成输入
# print('name= ',name);

# name=input('please enter your name:')
# print('name= ',name);
# --------------------------------------------------
# day02
# 变量
# 变量不需要指定数据类型
a = 1
str = 'hello'
answer = True

print(a,str,answer)

# 常量
NAME="wangyi"
print(NAME)

# 字符串
str=b'abc' # bytes类型的数据用b作为前缀
# 编码
print('abc'.encode('ascii'))
print('你好'.encode('utf-8'))
# 解码
print(b'abc'.decode('ascii'))
print(b'efg'.decode('utf-8'))
print('你好'.encode('utf-8').decode('utf-8'))
# 计算字符串长度
print(len(b'abc'))
print(len('你好'.encode('utf-8')))

# 格式化输出字符串
print('hello, %s'%'world')
print('hello, %s, welcome to %s' %('李四','北京'))
print('you have %d money' %10000)
# 输出指定长度
print('%5d' %5)
# 补零
print('%05d' %4)
# 指定小数位数
print('%.2f' %3.1415926)
# format()函数，使用传入参数替换字符串内的占位符{0}，{1}…….
print('hello,{0}, 成绩提升了{1:.1f}%'.format('李四',15.155))
# --------------------------------------------------