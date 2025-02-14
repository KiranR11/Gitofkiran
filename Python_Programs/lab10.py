import time

def fun(func):
	def fun2(*args,**kwargs):
		st=time.time()
		result=func(*args,**kwargs)
		et=time.time()
		print("The time taken is : %3.2fms"%((et-st)*10**6))
		return result
	return fun2

@fun
def fibo(n):
	a,b=0,1
	for i in range(n):
		yield a
		a,b=b,a+b

n=int(input("Enter value : "))
fibonacci=fibo(n)

print("series")
for i in range(0,n):
	print(next(fibonacci))
