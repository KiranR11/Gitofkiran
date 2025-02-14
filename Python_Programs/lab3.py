d=dict()
class Employee:
	def input(self):
		self.name=input("Enter Name\n")
		self.adds=input("Enter address\n")
		self.pan=input("Enter pan\n")
		self.basic=int(input("Enter basic salary\n"))
		self.tds=int(input("Enter tds\n"))
		self.deduct=int(input("Enter deduction amount\n"))
		self.hra=1.25*self.basic
		self.ta=0.25*self.basic
		self.gross=self.basic+self.hra+self.ta
		self.net=self.gross-self.deduct
		self.update()
	def update(self):
		d.update({self.name:{"name":self.name,"adds":self.adds,"pan":self.pan,"basic":self.basic,"tds":self.tds,"deduct":self.deduct,"hra":self.hra,"ta":self.ta,"gross":self.gross,"net":self.net}})
	def search(self,name):
		flag=0
		for key in d:
			if(key==name):
				print("Employee found")
				for i in d[key]:
					print(i,d[key][i])
					flag=1
		if(flag==0):
			print("Employee not found")
	def printemp(self):
		for key in d:
			print(key,d[key])

class employee(Employee):
	e1=Employee()
	while(True):
		ch=int(input("1.To input\n2.Update\n3.display\n4.search\n5.Exit\n"))
		if(ch==1):
			e1.input()
		if(ch==2):
			e1.update()
		if(ch==3):
			e1.printemp()
		if(ch==4):
			name=input("Enter name to search")
			e1.search(name)
		if(ch==5):
			break
	
