class machine():
	def cal(self):
		pass

class plus(machine):
	def cal(self,a,b):
		print(a+b)

class minus(machine):
	def cal(self,a,b):
		print(a-b)

class multiply(machine):
	def cal(self,a,b):
		print(a*b)

class divide(machine):
	def cal(self,a,b):
		print(a/b)


class factory():
	def method(self,way):
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