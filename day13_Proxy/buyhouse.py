""" a practise to proxy module """

class Me:
    """ the one to basic"""
    def findhouse(self):
        return "永和方便"
    def priceTooHigh(self):
        return "13000太貴啦"
    def defendPrice(self):
        return "學生沒錢QQ"
    def finish(self):
        return "謝謝"

class Agent(Me):
    """proxy one"""
    def __init__(self,me = "Me"):
        self.me = me
    def find_house(self):
        print( self.findhouse())
        print("#help")
    def price_TooHigh(self):
        print( self.priceTooHigh())
        print( "#argueing")
    def defend_Price(self):
        print(self.defendPrice())
        print( "#argue strongly")
    def pay(self):
        print( "#process"    )
        print(self.finish())

def Test():
    """ client"""
    me = Agent()
    me.find_house()
    me.price_TooHigh()
    me.defend_Price()
    me.pay()

if __name__ == "__main__":
    Test()
