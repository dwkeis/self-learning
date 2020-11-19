"""try to perform a decorator module"""
class Resturant:
    """make a base class"""
    def __init__(self):
        pass


class Order(Resturant):
    """to take order from this class"""
    def salad(self):
        """to add dish into the list by calling method"""
        return Jumbo.addup('salad')
    def main(self):
        return Jumbo.addup('main')
    def soup(self):
        return Jumbo.addup('soup')
    def dessert(self):
        return Jumbo.addup('dessert')
    def set(self):
        """ define a set info """
        return Jumbo.addup('salad'),Jumbo.addup('main'),Jumbo.addup('soup')

""" make the list and default to have drinks in it"""
list1 = ['drink']

class Jumbo():
    """make a class to add things to list"""
    def addup(self):
        list1.append(self)
    def check(self):
        """ to checkout the list and reset it"""
        print(list1)
        list1.clear()
        list1.append('drink')


aa = Order()


aa.salad()
aa.main()
Jumbo().check()
print(list1)
aa.set()
print(list1)