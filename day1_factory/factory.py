class footballteam:
	def team(self):
		pass

class Arsenal(footballteam):
	def __init__(self,teamname):
		self.__name = teamname
	def team(self):
		print ("Arsenal plays at " + self.__name)

class Barcelona(footballteam):
	def __init__(self,teamname):
		self.__name = teamname
	def team(self):
		print ("Barca plays at " + self.__name)

class nations:
	def playat(self):
		pass

class england(nations):
	def playat(self):
		return Arsenal("England")

class spain(nations):
	def playat(self):
		return Barcelona("Spain")

if __name__ == "__main__" : 
	nations = england()
	club = nations.playat()
	club.team()
	nations = spain()
	club = nations.playat()
	club.team()





