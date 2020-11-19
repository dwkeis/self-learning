#trying to perform factory mode by football team and where they play

class footballteam:
	#build the basic class
	def team(self):
		pass

class Arsenal(footballteam):
	#define a team name arsenal base on footballteam class
	def __init__(self,place):
		self.__name = place
	def team(self):
		# it will show where they play by the place 
		print ("Arsenal plays at " + self.__name)

class Barcelona(footballteam):
	#define a team name barca base on footballteam class
	def __init__(self,place):
		self.__name = place
	def team(self):
		# it will show where they play by the place 
		print ("Barca plays at " + self.__name)

class nations:
	# basic of where they play
	def playat(self):
		pass

class england(nations):
	# define a place call england
	def playat(self):
		# will send back to Arsenal() where they play
		return Arsenal("England")

class spain(nations):
	# define a place call spain
	def playat(self):
		# will send back to barca() where they play
		return Barcelona("Spain")

if __name__ == "__main__" : 
	nations = england()
	club = nations.playat()
	club.team()
	nations = spain()
	club = nations.playat()
	club.team()





