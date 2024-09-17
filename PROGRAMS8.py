#RECURSIVE
def rfact(n):
   if n==0:
      return 1
   else:   
      return n*rfact(n-1)
x=int(input("Enter no"))
print("Factorial of ",x," is ",rfact(x))      
#FIBONACCI
def rfib(n):
    if n<=1:
       return 1
    else:
       return (rfib(n-1)+rfib(n-2))
a=int(input("How many terms?"))
if a<=0:
     print("Enter a positive integer")
else:
     print("Fibonacci sequence: ")
     print(0)
     for i in range(a-1):
          print(rfib(i))
#GCD
# Python code to demonstrate naive
# method to compute gcd ( Loops )

def computeGCD(x, y):

	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small + 1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
			
	return gcd

a = 60
b = 48

# prints 12
print ("The gcd of 60 and 48 is : ", end="")
print (computeGCD(60,48))
