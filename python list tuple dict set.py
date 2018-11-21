# -*_ coding: utf-8 -*-

# list []
username=['zhangsan','lisi','wanger']
print(username)
# 获取list元素的个数
print(len(username))
# 访问指定元素
print(username[1])
# 反序获取元素
print(username[-1])
# 向list中添加元素
username.append('zhaoliu')
print(username)
# 在指定位置插入元素
username.insert(1,'jack')
print(username)
# 删除list末尾的元素
username.pop()
print(username)
# 删除指定位置的元素
username.pop(2)
print(username)
# 使用range()函数生成一个整数序列
lr=list(range(5)) # [0,4]
print(lr)
print("---------------------------------------------------------")
# tuple ()
t=('phone','computer','tv')
print(t)
# 创建一个带有list的tuple
list_tuple=(1,'a',['aa','bb',3])
print(list_tuple)
print(list_tuple[2][0])
list_tuple[2][0]=5
print(list_tuple)
print("---------------------------------------------------------")
#dict {}
d={'zhangsan':99,"lisi":98,"wangwu":97}
print(d)
# 根据key访问dict中的元素
print(d['zhangsan'])
# 根据key更改dict中元素的值
d['lisi']=100
print(d)
# 判断key是否存在
print('lisi' in d)
# 获取key对应的值
print(d.get('lisi'))
# 根据key删除一个元素
d.pop('lisi')
print(d)
# 添加一个元素
d['zhaoliu']=40
print(d)
print("---------------------------------------------------------")
# set ([])
s=set([1,2,4])
print(s)
# 添加元素
s.add(5)
print(s)
s.add('lisi')
print(s)
# 删除元素
s.remove(1)
print(s)
# 两个set交并运算
s1=set([1,2,3,4,5,6])
s2=set([9,8,7,6,5,3,2,1])
print(s1&s2)
print(s1|s2)