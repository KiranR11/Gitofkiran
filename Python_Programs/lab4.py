from op import *

obj1=op()
obj2=op()

obj1.input()
obj2.input()

while(1):
	print("0.Exit\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Floordivision\n5.Power\n")
	ch=int(input("enter your choice"))
	if ch==0:
		break
	elif ch==1:
		#obj1.__add__(obj2)
		obj1+obj2
	elif ch==2:
		#obj1.__sub__(obj2)
		obj1-obj2
	elif ch==3:
		#obj1.__mul__(obj2)
		obj1*obj2
	elif ch==4:
		#obj1.__floor__(obj2)
		obj2//obj1
	elif ch==5:
		#obj1.__pow__(obj2)
		obj1**obj2
	else:
		print("Invalid input")
