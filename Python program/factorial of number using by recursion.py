
 # factorial of number using by recursion

n=int(input("enter the number : "))
def fact(n):
	if n==0 or n==1:
		return 1
	return n*fact(n-1)
print(fact(n))