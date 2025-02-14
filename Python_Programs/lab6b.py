class calc:
	def area(self,l=None,b=None):
		if l is None and b is None:
			return 0
		elif l is not None and b is None:
			self.l=l
			return self.l*self.l
		elif l is not None and b is not None:
			self.l=l
			self.b=b
			return self.l*self.b
		else:
			print("Invalid input")

c=calc()
a=c.area()
print(a)
b=c.area(4)
print(b)
d=c.area(3,2)
print(d)
