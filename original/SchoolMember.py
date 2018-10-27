class SchoolMember:
    '''Represent any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialize SchoolMember:{})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end='')

class Teacher(SchoolMember):
    '''Represent a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represent a Student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))

if __name__ == '__main__':
    t = Teacher('Mrs.Wang', 28, 7000)
    s = Student('xiaoming', 12, 59)
    print()
    members = [t, s]
    for member in members:
        member.tell()
