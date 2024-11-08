class Dog:  ## 类名首字母一般大写
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
        enemy.blood = enemy.blood - self.power

# 创建实例
d1 = Dog(name="大黄",height=1.2,power=20)
d2 = Dog(name="小黑",height=1.5,power=30)

# 访问和修改属性
print(d1.power)
d1.power = 25
print(d1.power)

# 调用方法
d1.bark()
d2.attack(d1)
d1.bark()
