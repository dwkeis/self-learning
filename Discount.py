class DiscountStrategy:
    def __init__(self):
        pass

class MinusDiscount(DiscountStrategy):
    def calculate(self,value,discount):
        result = value - discount
        return result

class MultiplyDiscount(DiscountStrategy):
    def calculate(self,value,discount):
    	result = value * discount
    	return result


class NoDiscount(DiscountStrategy):
    def calculate(self,value,discount=0):
        return value

class Price:
    def __init__(self,discount_type,value,discount):
        self.discount_type = discount_type
        self.value = value
        self.discount = discount
        
    def calculate(self):
        list1 = []
        list1.append(self.discount_type.calculate(self.value,self.discount))
        print(list1)
    def checkout(self):
        print(sum(list1))


class Drink:
    def price(self):
        pass

class Milk(Drink):
    def output(self,price):
        self.price = price
        print("Milk : %s"%(self.price))

class Coffee(Drink):
    def output(self,price):
        self.price = price
        print("Coffee : %s"%(self.price))

if __name__ == '__main__':
    product = MinusDiscount()
    product = Price(product,10,3).calculate()

    product = MultiplyDiscount()
    product = Price(product,10,0.4).calculate()

    new = Milk()
    new.output(20)







