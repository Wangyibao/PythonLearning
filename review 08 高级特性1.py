# 1 切片
# 对于取指定索引范围的数，用循环麻烦，Python提供了切片（Slice）操作来简化操作。

# 定义一个List
arr=['zhangsan','lisi','wanger']

# 访问arr前两个元素
arr[0:2]

# 0可以省略
arr[:2]

# 获取最后一个元素
arr[-1:]

# 获取倒数两个元素
arr[-2:]


# 创建一个List
ll=list(range(50))

# [0,12)范围内，每两个取一个数
ll[:12:2]

# 所有数中，每6个取一个数
ll[::6]

# 2 迭代
# 如果给定一个list或tuple，可以通过for循环来遍历，这种遍历称为迭代（Iteration）。

# 创建一个dict
grade_map={'lisi':99,'zhangsan':94,'wanger':100}

# 迭代操作，迭代 key
for key in grade_map:
    print(key)

# 迭代操作，迭代 value
for value in grade_map.values():
    print(value)

# 迭代 key&value
for k,v in grade_map.items():
    print(k,':',v)

# 3 列表生成式
# 即 List Comprehensions，是Python内置的非常简单却强大的用来创建list的生成式。

# 生成list
list(range(1,11))


# 列表生成式，生成[1,11)范围内偶数的平方的列表
[x*x for x in range(1,11) if x%2 == 0]


# 使用两层循环
[m + n for m in 'abc' for n in 'xyz']


# 使用列表生成式输出grade_map的key-value对
[k+'='+str(v) for k,v in grade_map.items()]
