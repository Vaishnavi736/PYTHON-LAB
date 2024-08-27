#FUNCTION CREATION
def func():
    print("Hello")
func()
def func1(a,b):
    print(a+b)
func1(6,4)
def func2(*tab):
     print(tab)
     for i in tab:
          print(i)        
func2("oh","my","god",1,2,3)     
#
def arithmetic(a,b)
    print("Addition= ",a+b)
def subtract(a,b)
    print("Subtraction= ",a-b)
def mul(a,b)
    print("Multiplication= ",a*b)
def div(a,b)
    print("Division= ",a/b)            
def floordiv(a,b)
    print("Floor Division= ",a//b)
def moddiv(a,b)
    print("Modulo Division= ",a%b)
#ARITHMETIC OPERATIONS
def arithmetic(a,b):
    print("The Result : ")
    print("Addition= ",a+b)
    print("Subtraction= ",a-b)
    print("Multiplication= ",a*b)
    print("Division= ",a/b)            
    print("Floor Division= ",a//b)
    print("Modulo Division= ",a%b)
arithmetic(10,5)
#MULTIPLE RETURN VALUES
def func(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    return add,sub,mul
result= func(9,5)    
add,sub,mul=result
print("addition: ",add)
print("subtract: ",sub)
print("multiply: ",mul)
#GCD
def mul(a,b):
   return a*b
 
def lcm(a,b):   
   if(a>b):
      big=a
   else:
     big=b
   while(True):
      if(big%a==0 and big%b==0):
           return big
           break
      big+=1
   
def gcd(a,b):
     return (mul(a,b))//(lcm(a,b))      
ans=gcd(7,9)     
print("GCD is "+ str(ans))       
#LARGEST AND SMALLEST IN A LIST
def large(l):
    max=l[0]
    for i in l:
        if(i>max):
            max=i
    print(max)
def small(l):
    min=l[0]
    for i in l:
        if(i<min):
            min=i
    print(min)
large([4,3,5,7])             
small([4,3,5,7])             
#second large
def large(l):
    max=l[0]
    for i in l:
        if(i>max):
            max=i
    l.remove(max)
    max=l[0]
    for i in l:
        if(i>max):
            max=i
    print(max)
large([4,3,5,7])             
#CHECK
def func(*l):
    print(l)
    for i in l:
        print(i)
func([4,6,2,65],[4,4,7,4,7],[95,4,8,54,3])   
        
        
