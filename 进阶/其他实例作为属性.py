class Dog:
    def __init__(self, name, height, power):
        self.name = name
        self.height = height
        self.blood = 100  # 有的属性可以在模版直接创建
        self.power = power

    def bark(self):
        print(f'My name is {self.name},My blood is {self.blood}')

# 宠物犬
class PetDog(Dog):
    def __init__(self,name,height,power,price,house):
        super().__init__(name,height,power)
        self.price = price
        self.house = house

    def sing(self):
        print("I'm singing a song.")

class PetHouse():
    def __init__(self):
        print("PetHouse is created.")

# 创建实例
house = PetHouse()
pd = PetDog('Pet',1.5,15,1500,house)

