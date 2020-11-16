class footballteam:
	def team(self):
		pass

class Arsenal(footballteam):
	def __init__(self,teamname):
		self.__name = teamname
	def team(self):
		print ("Ozil plays at " + self.__name)

class player:
	def playat(self):
		pass

class ozil(player):
	def playat(self):
		return Arsenal("Arsenal")

if __name__ == "__main__" : 
	player = ozil()
	club = player.playat()
	club.team()





class Barcelona(footballteam):
	def team(self,teamname):
		print ("Team Barca")