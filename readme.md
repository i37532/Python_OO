# Python面向对象

[视频LINK](https://www.bilibili.com/video/BV1uE411x76i?spm_id_from=333.788.player.switch&vd_source=ef2483e6c9fc0260d768b09282b7d179&p=4)

## 1.\_\_init\_\_函数

```
构造方法
此处self可以理解为类的实例化的地址，如d1 = Dog()，d1即为一个实例，self指向实例地址
```

## 2.类方法

```
类方法:可以通过类名调用，也可以通过实例名调用
1.类方法不能访问实例变量，可以访问类变量
2.类方法需要加上@classmethod，第一参数必须是class(cls)
```

## 3.静态方法

```
#静态方法：不依赖实例和属性
使用@staticmethod
```

## 4.继承

```
class 子类(父类):
# super() 调用父类的方法
```

## 5.命名规则

```
1.类名：驼峰，SheepDog
2.方法名、变量名、参数、文件名：
全小写，下划线连接,如 num_of_sheeps
3.私有属性：变量名前加下划线 _secret 
```





