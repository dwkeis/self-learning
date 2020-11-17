class Drink:
    def __init__(self,sugar_num=0,ice_num=0):
        self.sugar = ["REGULAR","LESS","HALF","QUARTER","FREE"]
        self.ice = ["REGULAR","EASY","FREE","HOT"]

Drink()
class Tea(Drink):
    def __init__(self,sugar_num=0,ice_num=0):
        super().__init__(sugar_num,ice_num)
        print(sugar[sugar_num],ice[ice_num])

    def teaType(tea_num=0,sugar_num=0,ice_num=0):
        tea = ["LEMON","OOLONG","GINGER","HONEY"]
        print(tea[tea_num])

Drink()
drinks=Tea(1,1)
