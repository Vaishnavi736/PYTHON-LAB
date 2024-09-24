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
#KEY EXISTS OR NOT
mydict={1:"class",2:"crew",3:72,4:"lab"}
key=int(input("Enter key"))
if key in mydict:
        print("Key exists")
else:
      print("Key does not exists")
#ADD KEY VALUE PAIR
mydict={1:"class",2:"crew",3:72,4:"lab"}
mydict.update({5:"cse"})
print(mydict)
#SUM OF ITEMS IN A DICT
mydict={1:"class",2:"crew",3:"python",4:"lab"}
sum=" "
for i in mydict.values():
    sum=sum+i+" "
print("sum of all items ",sum)    
#second example
mydict={1:84,2:34,3:22,4:21}
sum=0
for i in mydict.values():
    sum=sum+i
print("sum of all items ",sum)    
#161
#LAMBDA FUNCTION FOR ODD AND EVEN
v=lambda n:n%2
x=int(input("Enter number"))
if v(x)==0:
    print("Even")
else:
    print("Odd")
    
        
