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
     for i in range(a):
          print(rfib(i))     
          
      
