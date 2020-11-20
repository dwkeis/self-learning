class Test:
	def __init__(self):
		print("default")
	def trytry(self):
		print("output")

class child(Test):
	def hello(self):
		print("child")

child = child()
