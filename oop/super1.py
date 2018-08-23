class Parent1(object):
    def __init__(self):
        super().__init__()
        print("is Parent1")
        print("goes Parent1")

class Parent2(object):
    def __init__(self):
        super().__init__()
        print("is Parent2")
        print("goes Parent2")

class Child1(Parent1):
    def __init__(self):
        print("is Child1")
        super().__init__()
        #Parent1.__init__(self)
        print("goes Child1")

class Child2(Parent1):
    def __init__(self):
        print("is Child2")
        super().__init__()
        #Parent1.__init__(self)
        print("goes Child2")

class Child3(Parent2):
    def __init__(self):
        print("is Child3")
        super().__init__()
       # Parent2.__init__(self)
        print("goes Child3")

class Grandson(Child1,Child2,Child3):
    def __init__(self):
        print("is Grandson")
        Child1.__init__(self)
        Child2.__init__(self)
        Child3.__init__(self)
        print("goes Grandson")


if __name__=="__main__":
    Grandson()
