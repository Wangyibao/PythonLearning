# 返回函数
def then_sum(*args):
    def cal_sum():
        sum=0
        for n in args:
            sum=sum+n
        return sum
    return cal_sum

f=then_sum(1,2,3,4)
print(f())
print('--------------------------')
# 匿名函数
ll=list(map(lambda x: x*x,[1,2,3,4]))
print(ll)
# 把匿名函数赋值给一个变量
nf=lambda x: x+x
print(nf(5))

# 把匿名函数当返回值返回
def nff(x,y):
    return lambda : x*x+y*y

print(nff(3,4)())
print('--------------------------')