class Students:
    department = 'Science'
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    # instancse method
    def display(self):
        print('Name',self.name)
        print('Roll',self.roll)

    #class level method
    @classmethod
    def info(cls,sec):
        print('I am CLass Mthod {} walks with {} lEgs...'.format(sec, cls.department))

    # Static method
    @staticmethod
    def sum(a,b):
        print('I am Static Method', a+b)


s = Students('Mahbub',1001)
s.info('Men')
s.sum(10,20)

