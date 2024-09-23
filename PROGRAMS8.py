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
       return n
    else:
       return (rfib(n-1)+rfib(n-2))
a=int(input("How many terms?"))
if a<=0:
     print("Enter a positive integer")
else:
     print("Fibonacci Sequence: ")
     for i in range(a):
          print(rfib(i))
#GCD
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter a"))
b=int(input("Enter b"))
print("GCD is ",gcd(a,b))
        
