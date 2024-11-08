class Dog:  ## 类名首字母一般大写
    # 构造方法
    # 此处self可以理解为类的实例化的地址，如d1 = Dog()，d1即为一个实例，self指向实例地址
    def __init__(self, name, height, blood, power):
        self.name = name
        self.height = height
        self.blood = blood
        self.power = power

d1 = Dog(name="大黄",height=1.2,blood=100,power=20)  # 创建实例

print(d1.name)
