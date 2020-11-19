""" try to do a drink shop """
class Drink:
    """drink should have sugar and ice section so are they"""
    def sugar(self,sugar_num=0):
        sugar = ["REGULAR","LESS","HALF","QUARTER","FREE"]
        print("sugar of your drink %s"%(sugar[sugar_num]))
    def ice(self,ice_num=0):
        ice = ["REGULAR","EASY","FREE","HOT"]
        print("ice of your drink %s "%(ice[ice_num]))


class Tea(Drink):
    """ base on drink you can choose tea"""
    def Type(self,tea_num=0):
        """ tea have various type"""
        tea = ["LEMON","OOLONG","GINGER","HONEY"]
        print("Drinks you order : %s"%(tea[tea_num]))

class Coffee(Drink):
    """ you can choose coffee also"""
    def Type(self,coffee_num=0):
        """ sure they have many type"""
        coffee = ["LATTE","MOCHA","FLAT_WHITE","BLUE_MOUNTAIN","AMERICANO","ESPRESSO"]
        print("Drinks you order : %s"%(coffee[coffee_num]))

class Order:
    """ to order what you want"""
    def __init__(self,product,flavor,sugar,ice):
        self.product = product
        self.flavor = flavor
        self.sugar = sugar
        self.ice = ice
    def choice(self):
        """ use to print out result by calling their own method with the value given"""
        self.product.Type(self.flavor)
        Drink.sugar(self.sugar)
        Drink.ice(self.ice)

order = Tea()
Order(order,1,1,2).choice()

order = Coffee()
Order(order,2,0,1).choice()
