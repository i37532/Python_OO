# 4 人数:
# 在为完成练习1的Car类中，添加一个名为number_of_people的属性，并将其默认值设置为0。添加一个名为max_people的属性，表示车上最多可以有几个人。修改相应的构造方法，传入max_people的值。
# 添加一个名为set_people() 的方法，它让你能够设置车上的人数，但是不能超过max_people的限制。
# 添加一个名为increase_people()的方法，每次调用这个方法就会让车上的人数加1，但是不能超过max_people的限制。
# 添加一个名为reduce_people()的方法，每次调用这个方法就会让车上的人数减少1，但是最多减少为0.
# 根据这个类创建一个名为car的实例，先通过属性直接打印其两个属性，再调用上面的两个方法。;
# 打印有多少人在车上，然后多次调用以上3个方法，并打印车上的人数。

class Car:
    def __init__(self, name, brand, max_people):
        self.name = name
        self.brand = brand
        number_of_people = 0
        self.max_people = max_people

    def show(self):
        print(self.name, self.brand)
    def run(self):
        print(f'The {self.name} is running.')
    def set_people(self,people):
        if people < self.max_people:
            self.number_of_people = people
        else:
            print("超员了宝贝")
    def increase_people(self):
        if self.number_of_people < self.max_people:
            self.number_of_people += 1
        else:
            print("不能再加啦，满员了")
    def reduce_people(self):
        if self.number_of_people > 0:
            self.number_of_people -= 1
        else:
            print("已经没人咯")

car = Car("Lala","Benz",max_people=5)
car.show()
car.run()
car.set_people(2)
car.increase_people()
car.increase_people()
car.increase_people()
car.increase_people()
car.increase_people()
car.reduce_people()
car.reduce_people()
car.reduce_people()
car.reduce_people()
car.reduce_people()
car.reduce_people()