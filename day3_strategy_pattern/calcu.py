"""performing a calculator """

class Machine():
    """ basic class of it """
    def cal(self):
        """bassic"""
        pass

class Plus(Machine):
    """ Plus method """
    def cal(self,a,b):
        """ show the result """
        print(a+b)

class Minus(Machine):
    """ Minus method """
    def cal(self,a,b):
        print(a-b)

class Multiply(Machine):
    """ mutiply method """
    def cal(self,a,b):
        print(a*b)

class Divide(Machine):
    """devide method """
    def cal(self,a,b):
        print(a/b)


class factory():
    """ a factory to produce which method will gonna use """
    def method(self,way):
        """define the input and returning to different method """
        if way == '+':
            return Plus()
        if way == '-':
            return Minus()
        if way == '*':
            return Multiply()
        if way == '/':
            return Divide()

if __name__ == '__main__':
    factory = factory()
    factory.method('*').cal(2,3)
    factory.method('-').cal(2,3)
    Plus().cal(2,3)
