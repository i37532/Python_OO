class Dog:  ## 类名首字母一般大写
    # 类属性
    dogs = []  # 保存每只狗

    # 类方法
    @classmethod
    def num_of_dogs(cls):
        return len(cls.dogs)
    @classmethod
    def biggest_dog(cls):
        max_height = -5
        for dog in cls.dogs:
            if dog.height > max_height:
                max_height = dog.height
        return max_height

    #静态方法：不依赖实例和属性
    @staticmethod
    def intro():
        print("This is a class about dogs.")

    # 构造方法
    # 此处self可以理解为类的实例化的地址，如d1 = Dog()，d1即为一个实例，self指向实例地址
    def __init__(self, name, height, power):
        self.name = name
        self.height = height
        self.blood = 100  # 有的属性可以在模版直接创建
        self.power = power
        Dog.dogs.append(self)


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

# 调用静态方法
Dog.intro()

