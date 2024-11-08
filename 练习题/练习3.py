# 3. Pig:
# 创建一个名为Pig的类，其中包含属性name和weight
# 定义一个名为show()方法，打印Pig的基本信息;
# 再定义一个名为run() 的方法，打印：'XX: 没吃过猪肉，让你看看猪跑！'。
# 创建多个表示不同猪的实例，并对每个实例都调用上述两个方法

class Pig:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def show(self):
        print(f'Pig {self.name} has a weight of {self.weight}')
    def run(self,name):
        print(f'{name}: 没吃过猪肉，让你看看猪跑！')

pig1 = Pig(name="Charlotte", weight=100)
pig1.show()
pig1.run("Lxh")

pig2 = Pig(name="Jack", weight=200)
pig2.show()
pig2.run("MinYoung")