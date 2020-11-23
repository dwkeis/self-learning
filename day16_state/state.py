class State:
	def temp(self):
		pass
	def vib(self):
		pass
	def twodec(self,value):
		self.value = value
		return '{:f}'.format(value)

class Metric(State):
	def display_temp(self,value):
		print("Meter : ")
		return twodec(value)
class Eng(State):
	def display_temp(self,value):
		print("Sausage : ")
		return twodec(value)

class MetricSystem:
	def State(self,country = "Metric()"):
		self.country = country
		return country

me = MetricSystem()
me = me.State()