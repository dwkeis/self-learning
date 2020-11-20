"""first draft to learn observe mode"""

class Observer:
    def update(self):
        pass

class Eng(Observer):
    def update(self):
        print("receive : eng")
        self.listen()
    def listen(self):
        print("Listened to eng")
   
class Pop(Observer):
    def update(self,way):
        print("receive : %s"%way)

class Observed:
    def addthings(self):
        self.action.update()
class SmokeSensor(Observed):
    def setAction(self,action):
        self.action=action

eng = Eng()
pop = Pop()

a = Observed()

smoke = SmokeSensor()
smoke.setAction(eng)
smoke.addthings()
