class check:
	def add(self,a=None,b=None):
		if type(a)==int and type(b)==int:
			print("Addition of two number",a+b)
		elif type(a)==str and type(b)==str:
			print("Concatination of strings ",a+b)

c=check()
c.add(2,3)
c.add("Abc","def")
