t1=(1,2,3,4)
t2=("a","b","c","d")
f=1
while(f):
	print("1.concatination\n2.length\n3.repeat factor\n4.membership\n5.count\n6.Maximum\n7.Minimum\n8.Slicing\n9.equality\n10.reverse\n11.Exit")
	c=int(input("Enter your choice"))
	if(c==1):
		print(t1+t2)
	elif(c==2):
		print(len(t1))
		print(len(t2))
	elif(c==3):
		print(t1*2)
		print(t2*2)
	elif(c==4):
		print(2 in t1)
		print("ab" in t2)
	elif(c==5):
		print(t1.count(3))
		print(t2.count("b"))
	elif(c==6):
		print(max(t1))
		print(max(t2))
	elif(c==7):
		print(min(t1))
		print(min(t2))
	elif(c==8):
		print(t1[0:3])
		print(t2[0:2])
	elif(c==9):
		print(t1 is t2)
	elif(c==10):
		print(t1[::-1])
		print(t2[::-1])
	elif(c==11):
		f=0
	else:
		print("Invalid input")
