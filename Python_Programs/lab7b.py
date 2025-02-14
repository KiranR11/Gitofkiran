class Animal:
	def walk(self):
		pass
	def communication(self):
		pass

class Cat(Animal):
	def walk(self):
		return "Cat is walking"
	def communicate(self):
		return "meow"

class Dog(Animal):
	def walk(self):
		return "Dog is walking"
	def communicate(self):
		return "whoof"

D=Dog()
C=Cat()
print(D.walk())
print(D.communicate())
print(C.walk())
print(C.communicate())
