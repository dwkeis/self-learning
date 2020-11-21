""" command mode practise """
class Light:
    """ build a basic class"""
    def update(self):
        pass

class Turnon(Light):
    """turnon function"""
    def update(self):
        print("light on")

class Turnoff(Light):
    """turnoff function"""
    def update(self):
        print("light off")

class Brighter(Light):
    """lights brighter function"""
    def update(self):
        print("light birghter")

class Dimmer(Light):
    """lights dimmer function"""
    def update(self):
        print("light dimmer")

class Remote:
    """make a remote to control the flow"""
    list1 = []
    def Add_command(self,order):
        """ put the action you want into a list"""
        self.list1.append(order)
    def Do_command(self):
        """simple loop the list and do the action"""
        for things in self.list1:
            things.update()



if __name__ == "__main__":
    turnon = Turnon()
    turnoff = Turnoff()
    brighter = Brighter()
    dimmer = Dimmer()

    remote = Remote()
    remote.Add_command(turnon)
    remote.Add_command(brighter)
    remote.Add_command(brighter)
    remote.Add_command(dimmer)
    remote.Add_command(dimmer)
    remote.Do_command()
