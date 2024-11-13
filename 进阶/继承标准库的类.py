import turtle as t

class MyTurtle(t.Turtle):
    def big_circle(self):
        self.color('blue')
        self.circle(200)

s = t.Screen()

my_turtle = MyTurtle()  # 创建 MyTurtle 的实例
my_turtle.big_circle()  # 调用实例的方法

s.mainloop()