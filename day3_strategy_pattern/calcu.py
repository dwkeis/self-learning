#performing a calculator

class machine():
	# basic class of it
	def cal(self):
		pass

class plus(machine):
	# plus method
	def cal(self,a,b):
		# show the result
		print(a+b)

class minus(machine):
	# minus method
	def cal(self,a,b):
		print(a-b)

class multiply(machine):
	# mutiply method
	def cal(self,a,b):
		print(a*b)

class divide(machine):
	#devide method
	def cal(self,a,b):
		print(a/b)


class factory():
	# a factory to produce which method will gonna use
	def method(self,way):
		#define the input and returning to different method
		if way == '+':
			return plus()
		if way == '-':
			return minus()
		if way == '*':
			return multiply()
		if way == '/':
			return divide()

if __name__ == '__main__':
	factory = factory()
	factory.method('*').cal(2,3)
	factory.method('-').cal(2,3)
	plus().cal(2,3)