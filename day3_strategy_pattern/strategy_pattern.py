"""build to perform a Strategy Pattern"""
class Fly():
    """ duck should / not fly so basic class"""
    def fly(self):
        pass

class FlyWithWings(Fly):
    """ can fly"""
    def fly(self):
        print("i know how to fly")

class NoFly(Fly):
    """ can't fly"""
    def fly(self):
        print("i walk on the ground")

class QuackQuack():
    """the sound the shout"""
    def quack(self):
        pass

class AhAh(QuackQuack):
    """ 1 way to shout"""
    def quack(self):
        print("i quack like AHAHAHAH")

class WaWa(QuackQuack):
    """ 2 way to shout"""
    def quack(self):
        print("i quack like WaWaWaWa")

class Duck():
    """ main class to use all the method above"""
    def __init__(self,fly_way,call_way):
        self.fly_way = fly_way
        self.call_way = call_way

    def fly(self):
        """ will call the flying way method and def under them, print out sentence"""
        self.fly_way.fly()

    def quack(self):
        """ will call the shouting way method and def under them, print out sentence"""
        self.call_way.quack()

if __name__ == '__main__':
    fly_gua_duck = Duck(FlyWithWings(), AhAh())
    fly_gua_duck.fly()
    fly_gua_duck.quack()

    no_fly_wa_duck = Duck(NoFly(), WaWa())
    no_fly_wa_duck.fly()
    no_fly_wa_duck.quack()
