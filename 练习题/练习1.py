# 1.汽车:
# 创建一个名为Car的类，其方法__init__() 设置两个属性:name和brand(品牌)。
# 定义一个名为show()的方法，功能是打印出汽车的名称和品牌。
# 定义一个名为run()的方法，打印:汽车XX跑起来了。其中XX表示汽车的name.
# 根据这个类创建一个名为car的实例，先通过属性直接打印其两个属性，再调用上面的两个方法。

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
