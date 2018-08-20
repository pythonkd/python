# 定义一个空的类
class  student():
    pass
#定义一个对象
mingyue=student()

class PythonStudent():

    name=None
    age=18
    course="Python"


    def doHomework(self):
        print('I 在做作业')

        #推荐在函数末尾使用return语句
        return None

#实例化一个叫yueyue的学生，是一个具体的人
yueyue=PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用
yueyue.doHomework()