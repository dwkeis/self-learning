#facade module trying

"""many complicate class here"""
class Sub_Class:
    def Method_One(self):
        print("1")
class Sub_Class_2:
    def Method_Two(self):
        print("2")
class Sub_Class_3:
    def Method_Three(self):
        print("3")
class Class_One:
    def Method_Four(self):
        print("4")

"""a facade to use all sub class"""
class Facade:
    def __init__(self):
        self.one = Sub_Class()
        self.two = Sub_Class_2()
        self.three = Sub_Class_3()
        self.four = Class_One()
    def Method_A(self):
        """using 2 method"""
        self.four.Method_Four()
        self.one.Method_One()
    def Method_B(self):
        """ 2method again"""
        self.two.Method_Two()
        self.three.Method_Three()

if __name__ == "__main__":
    facade = Facade()
    print("MethodA : ")
    facade.Method_A()
    print("MethodA : ")
    facade.Method_B()
