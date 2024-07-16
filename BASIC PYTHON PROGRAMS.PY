//FAHRENHEIT TO CELSIUS
f=float(input("enter f value"))
c=(f-32)*5/9
print("temperature in celsius is ",c)
//VOWEL AND CONSONANT
a=input()
b=['a','e','i','o','u','A','E','I','O','U']
if a in b:
    print("It's a vowel!")
else:
    print("It's a consonant!")   
//VALID TRIANGLE
a=int(input())
b=int(input())
c=int(input())
if(a+b>c):
   if(a+c>b):
      if(b+c>a):
         print("Valid triangle")
else:       
   print("Invalid triangle")  
//SWAP
x=int(input("enter a"))
y=int(input("enter b"))
x=x+y
y=x-y
x=x-y
print("after swap: ","x = ",x, "y = ",y) 
//SPEED
d=float(input("enter distance in km"))
t=float(input("enter time in min"))
s=d/t
print(s)
//SIMPLE INTEREST
p=float(input())
t=float(input())
r=float(input())
si=(p*t*r)/100
print("simple interest ",si)
//RECTANGLE
length=int(input())
breadth=int(input())
p=int(2*(length+breadth))
a=int(length*breadth)
print(p,a)
//LEAP YEAR
y=int(input())
if(y%4==0 and y%400==0 or y%100!=0):
   print("Leap year")
else:
   print("Non-leap year")   
//LARGEST
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
   print(a , " is large")
elif(b>a and b>c):
   print(b , " is large")
else:      
   print(c , "is large")
//GRADE
m=int(input("enter marks"))
if(m>=90):
   print("grade A")
elif(m>=80):
   print("grade B")
elif(m>=70):
   print("grade C")
elif(m>=60):
   print("grade D")
elif(m>=50):
   print("grade E")
else:
   print("Failed")
//EVEN AND ODD
a=int(input('enter a'))
if(a%2==0):
   print("Even!!")
else:  
   print("odd") 
//DAYS
day=int(input())
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
elif(day==4):
    print("Thursday")
elif(day==5):
    print("Friday")
elif(day==6):
    print("Saturday")
elif(day==7):
    print("Sunday")
else:
    print("invalid")
//CIRCLE
r=int(input("radius of the circle"))
c=2*3.14*r
print("circumference=",c)
//

