while True:
	print("1.Check value error\n2.Check File not Found Error\n3.Check Type Error\n4.Check IOError\n5.Check Name Error\n6.Exit\n")
	ch=int(input("Enter your choice"))
	if ch==1:
		try:
			f1=open("file1.txt",'d')
			print("Successfull")
		except ValueError:
			print("Caught Value Error")

	elif ch==2:
		try:
			f=open("file1.txt",'r')
			print("Successfull")
		except FileNotFoundError:
			print(" Caught File not Found Error")

	elif ch==3:
		try:
			f=open("file.txt",'r','w')
			print("Successfull")
		except TypeError:
			print("Type Error")
	elif ch==4:
		try:
			f=open('f1','w+')
			f.write("sample")
			f1=open('f2','r')
			print("Successfull")
		except IOError:
			print("Caught name error")

	elif ch==5:
		try:
			f=opens("f1",'r')
			print("successfull")
		except NameError:
			print("Caught Name Error")
	elif ch==6:
		break
	else:
		print("Invalid input")
