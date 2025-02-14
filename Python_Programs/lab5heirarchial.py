class Student:
	def __init__(self):
		self.name=input("Enter name:")
		self.usn=input("Enter usn:")
		self.age=int(input("Enter age:"))

	def display(self):
		print("Name : ",self.name)
		print("USN : ",self.usn)
		print("Age : ",self.age)

class Ugstudent(Student):
	def __init__(self):
		Student.__init__(self)
		self.sem=input("Enter semester")
		self.fees=int(input("Enter fees"))
		self.stipend=int(input("Enter stipend"))
		Ugstudent.display(self)

	def display(self):
		Student.display(self)
		print("Sem : ",self.sem)
		print("fees : ",self.fees)
		print("Stipend : ",self.stipend)

class Pgstudent(Student):
	def __init__(self):
		Student.__init__(self)
		self.sem=input("Enter your sem")
		self.fees=int(input("Enter fees"))
		self.stipend=int(input("Enter  stipend"))
		Pgstudent.display(self)
	def display(self):
		Student.display(self)
		print("Sem : ",self.sem)
		print("fees : ",self.fees)
		print("Stipend : ",self.stipend)

while(True):
	print("1.Ugstudent\n2.Pgstudent\n3.Exit")
	ch=int(input("Enter your choice:"))
	if ch==1:
		obj1=Ugstudent()	
	if ch==2:
		obj2=Pgstudent()
	if ch==3:
		break


 
