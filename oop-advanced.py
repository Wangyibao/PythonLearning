# 定义类
class Students(object):
    pass


# 给实例绑定属性和方法
s = Students()
s.name = "lisi"
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

'''注意：给一个实例绑定的方法，对另一个实例是不起作用的
    为了给所有实例都绑定方法，可以给class绑定方法
'''


def set_sex(self, sex):
    self.sex = sex


Students.set_sex = set_sex

s.set_sex('man')
print(s.sex)

s1 = Students()
s1.set_sex('woman')
print(s1.sex)


# 使用__slot__来限制给添加实例的属性
class Person(object):
    __slots__ = ('name', 'age')


p = Person()
p.name = 'zhangsan'
p.age = 18
# p.sex = 'man'  # 出错

'''注意：__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    除非在子类中也定义__slots__，这样子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''

# 使用@property

''' @property 装饰器负责把一个方法变成属性调用 '''

# 创建类
''' 把一个getter方法变成属性，只需要加上@property就可以，
    此时，@property本身又创建了另一个装饰器@score.setter，负责吧一个setter方法变成属性赋值
'''


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError("score must between 0-100!")
        self._score = value


s = Student()
s.score = 60
print(s.score)

print('---------- 定制类 ----------')


# 定制类

# __str__
class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('lisi'))


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'student object (name: %s)' % self.name


print(Student('lisi'))


# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


# __getitem__
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[1], f[2], f[3], f[4])


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[0:5])


# __getattr__
class Student(object):

    def __init__(self):
        self.name = 'lisi'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99


stu2 = Student()
print(stu2.name)
print(stu2.score)


class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25


stu3 = Student()
print(stu3.age())


# __call__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


stu4 = Student('lisi')
stu4()

print('---------- -----------')

from enum import Enum

# Month类型的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))

for name, member in Month._member_map_.items():
    print(name, '=>', member, ',', member.value)

# 更精确地控制枚举类型，从Enum派生出自定义类

from enum import Enum, unique


@unique  # 帮助检查保证没有重复值
class Weekday(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6


# 访问枚举类型
day1 = Weekday.mon
print(day1)

print(day1.value)

print(Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

print('=== ===')

# 先定义函数
def fn(self,name='world'):
    print('hello, %s' %name)
# 创建Hello类
Hello=type('Hello',(object,),dict(hello=fn))

h=Hello()
h.hello()
