class Dog:  ## 类名首字母一般大写
    # 类属性
    num_of_dogs = 0

    # 构造方法
    # 此处self可以理解为类的实例化的地址，如d1 = Dog()，d1即为一个实例，self指向实例地址
    def __init__(self, name, height, power):
        self.name = name
        self.height = height
        self.blood = 100  # 有的属性可以在模版直接创建
        self.power = power
    def bark(self):
        print(f'My name is {self.name},My blood is {self.blood}')
    def attack(self,enemy):
        enemy.reduce_blood(self.power)
    def reduce_blood(self,val):
        if self.blood > val:
            self.blood -= val
        else:
            self.blood = 0

# 创建实例
d1 = Dog(name="大黄",height=1.2,power=20)
d2 = Dog(name="小黑",height=1.5,power=30)

# 访问类属性
print(d1.num_of_dogs)
print(Dog.num_of_dogs)

# 修改类属性
d1.num_of_dogs = 2  # 当实例属性和类属性相同时，优先访问实例属性（这里没有则创建一个
print(Dog.num_of_dogs)
Dog.num_of_dogs = 2
print(Dog.num_of_dogs)

