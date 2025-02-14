class Student:
	def __init__(self):
		self.name=None
		self.usn=None
		self.age=None

	def getdata(self):
		self.name=input("Enter Name ")
		self.usn=input("Enter usn ")
		self.age=int(input("Enter age "))

class Abc1(Student):
	def __init__(self):
		super().__init__()
		self.sub1=None
		self.sub2=None
		self.sub3=None
	def sub_mark(self):
		super().getdata()
		self.sub1=int(input("Enter sub1 marks"))
		self.sub2=int(input("Enter sub2 marks"))
		self.sub3=int(input("Enter sub3 marks"))

	def cal(self):
		total=self.sub1+self.sub2+self.sub3
		percentage=(total/300)*100
		return total,percentage

class Abc2(Abc1):
		def display(self):
			super().sub_mark()
			total,percentage=super().cal()
			print("Name : ",self.name)
			print("USN : ",self.usn)
			print("Age : ",self.age)
			print("Total : ",total)
			print("Percentage : ",percentage)

obj1=Abc2()
obj1.display()
