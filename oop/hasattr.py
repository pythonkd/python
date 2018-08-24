class Person(object):
    def __init__(self,name,age):
        self.__name=name
        self.age=age

a=Person("lili",18)
getattr(a,"gender",setattr(a,"gender","male"))
