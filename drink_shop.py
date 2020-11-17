class Drink:
    def __init__(self):
        pass

    def flavor(sugar_num=0,ice_num=0):
        sugar = ["REGULAR","LESS","HALF","QUARTER","FREE"]
        ice = ["REGULAR","EASY","FREE","HOT"]
        print("sugar of your drink %s, and ice of your drink %s "%(sugar[sugar_num],ice[ice_num]))


class Tea(Drink):
    def Type(self,tea_num=0):
        tea = ["LEMON","OOLONG","GINGER","HONEY"]
        print("Drinks you order : %s"%(tea[tea_num]))

class Coffee(Drink):
    def Type(self,coffee_num=0):
        coffee = ["LATTE","MOCHA","WHITE","BLUE_MOUNTAIN","AMERICANO","ESPRESSO"]
        print("Drinks you order : %s"%(coffee[coffee_num]))

class Factory:
    def choose(self,product):
        if product == 'tea':
            return Tea()
        if product == 'coffee':
            return Coffee()

factory = Factory()
factory.choose('tea').Type(1)
Drink.flavor(2,1)


