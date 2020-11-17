class Drink:
    def sugar(sugar_num=0):
        sugar = ["REGULAR","LESS","HALF","QUARTER","FREE"]
        print("sugar of your drink %s"%(sugar[sugar_num]))
    def ice(ice_num=0):
        ice = ["REGULAR","EASY","FREE","HOT"]
        print("ice of your drink %s "%(ice[ice_num]))


class Tea(Drink):
    def Type(self,tea_num=0):
        tea = ["LEMON","OOLONG","GINGER","HONEY"]
        print("Drinks you order : %s"%(tea[tea_num]))

class Coffee(Drink):
    def Type(self,coffee_num=0):
        coffee = ["LATTE","MOCHA","FLAT_WHITE","BLUE_MOUNTAIN","AMERICANO","ESPRESSO"]
        print("Drinks you order : %s"%(coffee[coffee_num]))

class Order:
    def __init__(self,product,flavor,sugar,ice):
        self.product = product
        self.flavor = flavor
        self.sugar = sugar
        self.ice = ice
    def choice(self):
        self.product.Type(self.flavor)
        Drink.sugar(self.sugar)
        Drink.ice(self.ice)

order = Tea()
order = Order(order,1,1,2)
order.choice()

order = Coffee()
order = Order(order,2,0,1)
order.choice()
