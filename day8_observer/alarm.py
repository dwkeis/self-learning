"""a test learn from online"""

class Observer:
    def update(self):
        pass

class AlarmSensor (Observer):
    def update(self, action):
        print ("alarm: %s" % action)
        self.runAlarm ()
    def runAlarm(self):
        print ("reporting...")

class WaterSprinker (Observer):
    def update(self, action):
        print ("split: %s" % action)
        self.runSprinker ()
    def runSprinker(self):
        print ("spliting...")

class EmergencyDialer (Observer):
    def update(self, action):
        print ("call: %s" % action)
        self.runDialer ()
    def runDialer(self):
        print ("calling...")


class Observed:
    observers=[]
    def addObserver(self,observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)
class smokeSensor(Observed):
    def setAction(self,action):
        self.action=action
    def isFire(self):
        return True

if __name__=="__main__":
    alarm=AlarmSensor()
    sprinker=WaterSprinker()
    dialer=EmergencyDialer()
 
    smoke_sensor=smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)
 
    if smoke_sensor.isFire():
        smoke_sensor.setAction("fire!")
        smoke_sensor.notifyAll()
