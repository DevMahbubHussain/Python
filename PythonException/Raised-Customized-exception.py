class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg

age = int(input('Enter Age : '))

if age > 60:
    raise TooYoungException('Please Wait......')
elif age < 18:
    raise TooOldException('All ready Done....')
else:
    print('Thanks....')