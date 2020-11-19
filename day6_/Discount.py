""" try to perform discount function when buy drinks"""

class DiscountStrategy:
    """ basic class"""
    def __init__(self):
        pass

class MinusDiscount(DiscountStrategy):
    """ just reduce price by minus a value"""
    def calculate(self,value,discount):
        result = value - discount
        return result

class MultiplyDiscount(DiscountStrategy):
    """ 60% off 50% off"""
    def calculate(self,value,discount):
        result = value * discount
        return result

class NoDiscount(DiscountStrategy):
    """ sorry no discount for you"""
    def calculate(self,value,discount=0):
        return value

class Price:
    """ the way to order and calculate price"""
    def __init__(self,what,value,discount_type,discount):
        self.discount_type = discount_type
        self.value = value
        self.discount = discount
        self.what = what
    def calculate(self):
        """ draft function which is not finished"""
        list1 = []
        money = self.discount_type.calculate(self.value,self.discount)
        list1.append(self.discount_type.calculate(self.value,self.discount))
        print(money)
    def checkout(self):
        """ want to put drinks in list and checkout tgt"""
        print(sum(list1))
    def product(self):
        """ define what drink you choose and the discounted value"""
        if self.what == 'milk':
            return Milk().output(self.discount_type.calculate(self.value,self.discount))
        if self.what == 'coffee':
            return Coffee().output(self.discount_type.calculate(self.value,self.discount))
            
class Drink:
    """ class of drink"""
    def price(self):
        pass

class Milk(Drink):
    """ you drink milk"""
    def output(self,price):
        """output the price"""
        self.price = price
        print("Milk : %s"%(self.price))

class Coffee(Drink):
    """you drink coffee"""
    def output(self,price):
        """output price"""
        self.price = price
        print("Coffee : %s"%(self.price))

if __name__ == '__main__':

    new = Milk()
    new.output(20)

    factory = MinusDiscount()
    factory = Price('coffee',20,factory,1)
    factory.product()
