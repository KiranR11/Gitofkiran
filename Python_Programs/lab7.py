class Employee:
	raise_amt=1
	def __init__(self,first,last,empid,pay):
		self.first=first
		self.last=last
		self.empid=empid
		self.pay=pay
	def apply_raise(self):
		self.pay=int(self.pay*self.raise_amt)
	def display(self):
		print("Name :",self.first,self.last)
		print("Empid: ",self.empid)
		print("Pay :",self.pay)
class Developer(Employee):
	raise_amt=2
	def apply_raise(self):
		#super().apply_raise()
		#super().__init__()
		self.pay=int(self.pay*self.raise_amt)
class Manager(Employee):
	raise_amt=3
	def apply_raise(self):
		#super().apply_raise()
		#super().__init()
		self.pay=int(self.pay*self.raise_amt)

emp1=Developer("Ravi","Singh",100,10000)
emp2=Manager("Raj","Roy",200,20000)
emp1.display()
emp2.display()
print("\nOVERRIDING ")
emp1.apply_raise()
emp2.apply_raise()

emp1.display()
emp2.display()
