class fries():
	def describe(self):
		pass

class noSalt(fries):
	def __init__(self,flavor):
		self.__name = flavor
	def describe(self):
		print("i am " + self.__name + " fries")

class default(fries):
	def __init__(self,flavor):
		self.__name = flavor
	def describe(self):
		print("i am " + self.__name + " fries")

class Factory:
	def product_fries(self, flavor):
		if flavor == 'nosalt':
			return noSalt("no salt")
		if flavor == 'original':
			return default("default")

if __name__ == '__main__':
	factory = Factory()
	factory.product_fries('nosalt').describe()
	factory.product_fries('original').describe()