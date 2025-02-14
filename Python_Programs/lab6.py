class greeting:
	def Hello(self,name=None,Age=None):
		if name is None and Age is None:
			print("Hello")
		elif name is not None and Age is None:
			print(f"Hello {name}")
		elif name is not None and Age is not None:
			print(f"Hello {name} and age is {Age}")
		else:
			print("Invalid input")

g=greeting()
g.Hello()
g.Hello("Aparna")
g.Hello("Aparna",21)
