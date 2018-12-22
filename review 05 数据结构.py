'''
1 list
    list，列表，一种有序的集合，可以随时添加和删除其中的元素。
'''
# 创建list
username=['lisi','zhangsan','wanger']


# 使用range()函数生成一个整数序列
list(range(5))


# 获取list元素的个数
len(username)


# 访问指定元素
username[2]


# 反序获取元素
username[-1]

username[-2]

username[-3]


# 向list中添加元素
username.append('zhaoliu')



# 在指定位置插入元素
username.insert(1,'jack')

# 删除list末尾的元素
username.pop()

username


# 删除指定位置的元素
username.pop(2)

username

'''
注意：
    list中的元素类型可以不同
    list中的元素也可以是list
    如果一个list中一个元素也没有，则长度为0
'''

'''
2 tuple
    tuple，元组，一种有序列表，一旦初始化就不能修改。
'''

# 创建tuple
mytuple=('phone','computer','tv')

'''
注意：
    tuple不能修改，没有append()，insert()这样的方法
    只有一个元素时，应在第一个元素后面加逗号
'''
onetuple=('phone',)

# 不加逗号结果
onetuple1=('phone')

# 如果tuple中含有list元素，则list可变
listtuple=(1,'a',['aa','bb',3])

# 更改tuple中list中的元素
listtuple[2][0]='cc'
listtuple[2][2]='55'

'''
3 dict
    dict，字典或称为map，使用键值对（key-value）存储。
'''
# 创建dict
mydict={'lisi':99, 'zhangsan':85, 'wangwu':88}

# 访问dict中元素
mydict['wangwu']


# 更改元素的值
mydict['wangwu']=95

mydict


# 判断key是否存在的两种方法
# 方法1
'wangwu' in mydict

# 方法2
mydict.get('wangwu')

# 如果key不存在，返回none，或者自己指定的value
mydict.get('liliu',-1)

mydict.get('liliu')

# 删除一个key，对应的value也会被删除
mydict.pop('zhangsan')

mydict


# 向dict中添加元素
mydict['wuqi']=86

{'lisi': 99, 'wangwu': 95, 'wuqi': 86}

'''
注意：
    dict内部存放的顺序和key放入的顺序是没有关系的
    与list比较，dict有以下特点： 
    1 查找和插入的速度极快，不会随着key的增加和变慢
    2 需要占用大量的内存
'''

'''
4 set
    set，集合，无序无重复元素的集合。
'''
# 创建set，需要提供一个list作为输入集合
myset=set([1,2,3])


# 重复元素会被删除
myset1=set([1,2,2,3,4,5,5])


# 通过add()方法可以添加元素到set中
myset.add(8)

# remove()方法可以删除set中元素
myset.remove(1)

# 交集、并集操作
mset1=set([1,2,3])
mset2=set([2,3,4])
mset1 & mset2

mset1 | mset2

