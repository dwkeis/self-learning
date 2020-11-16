"""build to perform a Strategy Pattern"""
class Fly():
    def fly(self):
        pass

class FlyWithWings(Fly):
    def fly(self):
        print("i know how to fly")

class NoFly(Fly):
    def fly(self):
        print("i walk on the ground")

class QuackQuack():
    def quack(self):
        pass

class AhAh(QuackQuack):
    def quack(self):
        print("i quack like AHAHAHAH")

class WaWa(QuackQuack):
    def quack(self):
        print("i quack like WaWaWaWa")

class Duck():
    def __init__(self,fly_way,call_way):
        self.fly_way = fly_way
        self.call_way = call_way

    def fly(self):
        self.fly_way.fly()

    def quack(self):
        self.call_way.quack()

if __name__ == '__main__':
    fly_gua_duck = Duck(FlyWithWings(), AhAh())  # 创建一个会飞会呱的鸭子
    fly_gua_duck.fly()
    fly_gua_duck.quack()

    no_fly_wa_duck = Duck(NoFly(), WaWa())  # 创建一个不会飞，只会哇哇叫的鸭子
    no_fly_wa_duck.fly()
    no_fly_wa_duck.quack()
