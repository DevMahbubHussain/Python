class Bird:
    wings = 2

    @classmethod

    def fly(cls,name):

        print('{} flying with {} legs'.format(name,cls.wings))

Bird.fly('Egle')
