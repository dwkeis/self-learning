"""trying to perform template module"""

class Boss:
    """ boss action """
    def think(self):
        return "you no good"
    def redo(self):
        return "you gotta redo"

class Manager(Boss):
    """ manager need to take action """
    def UI(self):
        return "find a UI"
    def boss_UI(self):
        return "UI result"
    def system(self):
        return "find system"
    def boss_system(self):
        return "system result"
    def complete(self):
        """print what boss think you """
        print(self.think())
        print(self.boss_UI())
        print(self.boss_system())
    def redoall(self):
        """print what boss want you to do """
        print(self.redo())
        print(self.UI())
        print(self.system())

manager = Manager()
manager.complete()
manager.redoall()
