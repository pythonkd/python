class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        print("Initialize {0}".format(self.name))
        Robot.population += 1
    def __del__(self):
        print('{} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print("There are still {0:d} robots working.".format(Robot.population))
    def sayHi(self):
        '''Greeting by the robot.
        Yeah, they can do that.'''
        print('Greetings, my master call me {}.'.format(self.name))
    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('c-3PO')
droid2.sayHi()
Robot.howMany()
print("Robots have finished their work.So let's destroy them.")
del droid1
del droid2

Robot.howMany()