while true:
	print("enter 1 for string manipulation:"
		"\n enter 2 for tuple manipulation"
		"\n enter 3 to exit")
	print("\n")
	chc=int(input("enter your choice:"))
	if chc==1:
        str1=input("enter a string:")
	    print("enter 1 to capitalize string"
		"\n enter 2 to convert to upper case"
		"\n enter 3 to convert to lower case"
		"\n enter 4 to concatenate two strings"
		"\n enter 5 to return length of strings"
		"\n enter 6 to remove leading whitespaces"
		"\n enter 7 to remove trailing whitespaces"
		"\n enter 8 to split a string"
		"\n enter 9 to find index of substring"
		"\n enter 10 to go back")
	    print("\n")
	    str_chc = int(input("enter your choices:"))
		print("entered string:",str1)
		if str_ch==1:
			print(str1.capitalize())
		elif str_chc==2:
			print(str1.upper())
		elif str_chc==3:
			print(str1.lower())
		elif str_chc==4:
			str2 = input("enter second string:")
			print(str1+str2)
		elif str_chc==5:
			print("length of string:",len(str1))
		elif str_chc==6:
			print(str1.lstrip())
		elif str_chc==7:
			print(str1.rstrip())
		elif str_chc==8:
			c=input("enter character to split:")
			print(str1.find(c))
		elif str_chc==10:
			rwt=input("Replace what?:")
			rwi=input("Replace with?:")
			print(str1.replace(rwt,rwi))
		elif str_chc==11:
			print("\n")
		elif chc==2:
    			tup1=tuple(input("enter tuple1:"))
			    print("enter 1 to find length of tuple"
				"\n enter 2 to return index of element"
				"\n enter 3 to no. of occueances of an element"
				"\n enter 4 to concatenate two tupels"
				"\n enter 5 to reverse tupel"
				"\n enter 6 to return max element"
				"\n enter 7 to return min element"
				"\n enter 8 to return sorted tuple"
				"\n enter 9 to find if specific element exists"
				"\n enter 10 for sum of elements:"
				"\n enter 11 to go back")
				print("\n")
				tup_chc=int(input("enter your choice:"))
				if tup_chc==1:
					print(len(tup1))
				elif tup_chc==2:
					c=input("enter element to find:")
					print(tup.index(c))
				elif tup_chc==3:
					c=input("enter element to find no. of occurances:")
					print(count(c))
				elif tup_chc==4:
					tup2=tuple(input("enter second tuple:"))
					print(tup1+tup2)
				elif tup_chc == 5:
					print(tup1[::-1])
				elif tup_chc == 6:
					print(max(tup1))
				elif tup_chc == 7:
					print(min(tup1))
				elif tup_chc == 8:
					print(sorted(tup1))
				elif tup_chc == 9:
					e = input("enter element:")
					print(e in tup1)
				elif tup_chc == 10:
					continue
				elif chc == 3:
					print("exiting")
					break
