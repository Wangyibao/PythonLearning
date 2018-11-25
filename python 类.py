# 定义类
class Person(object):
    # 定义方法
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.__sex=sex

    def get_sex(self):
        return self.__sex

    def set_sex(self,sex):
        self.__sex=sex

    def print_self(self):
        print('i am a person')

    def print_info(self):
        print('name: %s, age: %s, sex: %s' %(self.name,self.age,self.__sex))

print('-----------------------')
# 创建对象
lisi=Person('lisi','23','man')
lisi.print_info()
lisi.print_self()
print(lisi.get_sex())
print('-----------------------')
# 继承
class Students(Person):
    def study(self):
        print('i can study')

    def print_info(self):
        print('i am a student')

stu1=Students('wanger','22','man')
stu1.print_self()
stu1.print_info()
stu1.study()
print('-----------------------')
# 多态
def run(person):
    person.print_info()

run(Person('wanger','23','woman'))
run(Students('lisi','25','man'))
print('-----------------------')
# 实例熟悉和类属性
class Man(object):
    sex='man'

# 创建实例对象
mm=Man()
print(mm.sex)
print(Man.sex)
mm.sex='woman'
print(mm.sex)
print(Man.sex)
del mm.sex
print(mm.sex)