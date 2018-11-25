g=(x*x for x in range(10))
print(list(range(10)))

next(g)
next(g)

for n in g:
    print(n)

# 求斐波那契数列
def fib(num):
    n,a,b=0,0,1
    while n<num:
        print(b,end=" ")
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib(6))

# 使用生成器（generator）求斐波那契数列
def fib_g(num):
    n,a,b=0,0,1
    while n<num:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

fib_g(6)
for n in fib_g(6):
    print(n,end=" ")

