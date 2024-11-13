class Dog:
    def __init__(self, name, height, power):
        self.name = name
        self.height = height
        self.blood = 100  # 有的属性可以在模版直接创建
        self.power = power

    def bark(self):
        print(f'My name is {self.name},My blood is {self.blood}')

# 牧羊犬
class SheepDog(Dog):
    def __init__(self,name,height,power,num_of_sheeps):
        super().__init__(name,height,power)  # super() 调用父类的方法
        self.num_of_sheeps = num_of_sheeps
# 警犬
class PoliceDog(Dog):
    def __init__(self,name,height,power,ability):
        super().__init__(name,height,power)
        self.ability = ability


# 宠物犬
class PetDog(Dog):
    def __init__(self,name,height,power,price):
        super().__init__(name,height,power)
        self.price = price

# 创建实例
sd = SheepDog('jack',1.7,20,5)
print(sd.num_of_sheeps)
print(sd.blood)
sd.bark()

pd = PoliceDog('jhon',1.7,20,5)
pd.bark()
print(pd.ability)