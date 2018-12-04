# 读文件
# 1 打开文件对象，如果文件不存在，会抛出异常信息
f=open('/Users/Mac/mydata/iotest.txt','r') # r表示读

# 2 读取文件中的全部内容
str=f.read()
print(str)

# 3 关闭资源
f.close()