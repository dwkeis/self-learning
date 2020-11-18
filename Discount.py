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
        

class Checkout(Price):
    def calculate(self):
        super().calculate()
        print(sum(list1))


class Drink:
    def describe(self):
        pass

class Milk(Drink):
    def __init__(self,price=0):
        self.price = price
    def dd(self):
        print(self.price)

class Coffee(Drink):
    def __init__(self,price):
        self.price = price
    def price(self):
        print("milk : %s"%(self.price))

if __name__ == '__main__':
    product = MinusDiscount()
    product = Price(product,10,3)
    product.calculate()


    product = NoDiscount()
    product = Price(product,10,100)
    product.calculate()



