class Student(object):
    def __init__(self,name="NOname",age=18):
        self.name=name
        self.age=age

    def say(self):
        print("My name is {}".format(self.name))


def sayHello():
    print("Hi,欢迎来到图灵学院！")


if __name__=="__main__":
    print("我是模块p01")
