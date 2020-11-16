"""is a test for factory model"""
class Fries():
    """define fries"""
    def describe(self):
        pass

class NoSalt(Fries):
    """define fries without salt"""
    def __init__(self,flavor):
        self.__name = flavor
    def describe(self):
        print("i am " + self.__name + " fries")

class Default(Fries):
    """ it's the default  flavor of fries"""
    def __init__(self,flavor):
        self.__name = flavor
    def describe(self):
        print("i am " + self.__name + " fries")

class Factory:
    """where to make fries"""
    def product_fries(self, flavor):
        if flavor == 'nosalt':
            return NoSalt("no salt")
        if flavor == 'original':
            return Default("default")

if __name__ == '__main__':
    factory = Factory()
    factory.product_fries('nosalt').describe()
    factory.product_fries('original').describe()
