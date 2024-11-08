# 2. 5辆汽车:
# 根据在练习1而编写的类创建3个实例，并对每个实例调用方法show方法。

class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def show(self):
        print(self.name, self.brand)
    def run(self):
        print(f'The {self.name} is running.')
car = Car("Lala","Benz")
car.show()
car.run()

car2 = Car("Lala2","Benz2")
car2.show()
car2.run()

car3 = Car("Lala3","Benz3")
car3.show()
car3.run()
