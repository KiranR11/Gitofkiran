l1=[]
l2=[]
n1=int(input("Enter number of elements to l1 "))
n2=int(input("Enter number of elements to l2 "))
for i in range(0,n1):
        e=int(input("Element for l1:"))
        l1.append(e)

for i in range(0,n2):
        e=int(input("Element for l2:"))
        l2.append(e)

while(1):
        print("1.length\n2.sum\n3.Equality\n4.Repeat factor\n5.Maximum\n6.Minimum\n7.Concatination\n8.Reverse\n9.Mamebership10\n10.Slicing\n11.Exit")
        ch=int(input("Enter your choice"))
        if ch==1:
                print("length of l1",len(l1))
                print("length of l2",len(l2))
        elif ch==2:
                print("Sum of l1",sum(l1))
        elif ch==3:
                print("Is l1 and l2 same?",(l1==l2))
        elif ch==4:
                print("Repeat factor",l1*2)
        elif  ch==5:
                print("Max of l1",max(l1))
        elif ch==6:
                print("Min of l1",min(l1))
        elif ch==7:
                print("Concatination",l1+l2)
        elif ch==8:
                print("Reverse of l1",l1[::-1])
        elif ch==9:
                a=int(input("Enter element to check"))
                print("Checking membership",a,"in l1",(a in l1))
        elif ch==10:
                print("Slicing",l1[0:3])
        elif ch==11:
                break
        else:
                print("Invalid input")




