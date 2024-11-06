SET 1
1)
f=float(input())
c=(f-32)*5/9
print("Celsius: ",c)
2)
x=int(input())
y=int(input())
x=x+y
y=x-y
x=x-y
print(x,y)
3)
mydict={1:"comic",2:"chatterbox",3:"crew",4:70}
key=int(input("key"))
if key in mydict:
    print("Exists")
else:
    print("does not exists")
    

SET 2
1)
alpha=input("enter")
b=['a','e','i','o','u','A','E','I','O','U']
if alpha in b:
    print("vowel")
else:
    print("consonant")
2)
l=[]
n=int(input("Enter number"))
for i in range(n):
    ele=int(input("enter element"))
    l.append(ele)
print(l)
print("pos of min element",l.index(min(l)))
print("pos of max element",l.index(max(l)))
3)
def rfact(n):
    if n==0:
        return 1
    else:
        return n*rfact(n-1)
num=int(input("enter"))
print(rfact(num))
        

SET 3:
1)
l=[]
n=int(input("ENter num"))
for i in range(n):
    ele=int(input("enter element"))
    l.append(ele)
print(l)
print("sum ",sum(l))
print("avg: ",sum(l)/len(l))
2)
TEXT FILE
3)
def rfib(n):
    if n<=0:
        return n
    else:
        return (rfib(n-1)+rfib(n-2))
a=int(input("enter"))
if a<=0:
    print("enter positive")
else:
    print("fib seq:")
    for i in range(a):
        print(rfib(i))

SET 4:
1)
y=int(input("enter"))
if (y%4==0 and y%400==0 or y%100!=0):
    print("LEAP")
else:
    print("not leap")
2)
l1=["M","na","i","Abhi"]
l2=["y","me","s","Ram"]
l3=[]
for i in range(len(l1)):
   l3.append(l1[i]+l2[i])
print(l3)   
3)
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
    return mul(a,b)//lcm(a,b)
ans=gcd(8,4)
print("GCD ",str(ans))

SET 5:
1)
g=int(input("enter"))
if(g>=90):
    print("A grade")
elif(g>=80):
    print("B grade")
elif(g>=70):
    print("C grade")
elif(g>=60):
    print("D grade")
elif(g>=50):
    print("E grade") 
else:
    print("Failed")

2)
i)
x=int(input())
y=int(input())
z=int(input())
print("logical AND", x<y and z>y)
print("logical OR", x<y or z>y)
print("logical NOT", not(x<y))

ii)
x=int(input())
y=int(input())
z=int(input())
print("bitwise AND", x&y )
print(" bitwise OR", x|y )
print(" bitwise XOR", x^y )
print(" bitwise NOT",~x)
print("zerofill left shift ",x<<1)
print("unsigned right shift ",x>>1)

3)CSV FILE

SET 6:
1)
l=[]
n=int(input("ENter number"))
for i in range(n):
    ele=int(input("ENter element"))
    l.append(ele)
print(l)
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print("After interchanging :",l)

2)
s=input()
k=s.split()
for i in k:
    if(len(i)%2==0):
        print(i)
3)BINARY FILE

SET 7:

1)
l=[]
n=int(input("ENter number"))
for i in range(n):
    ele=int(input("ENter elem"))
    l.append(ele)
print(l)
even=[]
odd=[]
for i in range(n):
     if(l[i]%2==0):
         even.append(l[i])
    else:
        odd.append(l[i])
print(even)
print(odd)

2)
s=input()
rev=""
for i in s:
    rev=i+rev
print("Reverse: ",rev)    

3)
class Parent:
    def Method1(self):
        print("Method in Parent class")
class Child1(Parent):
    def Method2(self):
        print("Method in child1 class")
class Child2(Child1):
    def Method3(self):
        print("Method in Child2 class")
obj=Child2()
obj.Method1()
obj.Method2()
obj.Method3()

SET 8:
 1)
l=float(input("length"))
b=float(input("breadth"))
area=l*b
perimeter=2*(l+b)
print("area",area,"perimeter",perimeter)
2)
mydict={1:"cse",2:"it",3:"ece",4:"csbs"}
mydict.update({5:"eee"})
print(mydict)
3)
class add:
    def __init__(self,f,s):
         self.first=f
         self.second=s
    def display(self):
         print("First number ",self.first)
         print("second number: ",self.second)
         print("addition ",self.first+self.second)
obj=add(8,4)
obj.display()

SET 9:
1)
a=int(input())
b=int(input())
c=int(input())
if (a>b and a>c):
    print(a,"is big")
elif(b>c):
    print(b,"is big")
else:
    print(c,"is big")

2)
def secondlarge(l):
    large=l[0]
    for i in l:
        if(i>large):
            large=i
    l.remove(large)
    seclarge=l[0]
    for i in l:
        if(i>seclarge):
            i=seclarge
    print(seclarge)
list=[4,6,3,2]
print(seclarge(list))

3)
d=float(input("km"))
tm=float(input("min"))
th=tm/60
s=d/th
print("speed",s)

SET 10:

1)
i)
a=int(input())
b=int(input())
print("Arithmetic operations;  ")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
ii)
a=int(input())
b=int(input())
c=int(input())
print("Relational operations;  ")
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

iii)
a=int(input())
b=int(input())
c=int(input())
print("Identity operations;  ")
print(a is b)
print(a is not b)
print(c is a)


2)
a=int(input())
b=int(input())
c=int(input())
if(a+b>c):
    if(b+c>a):
        if(a+c>b):
            print("Valid triangle")
else:
    print("Invalid triangle")


3)
s=input()
rev=""
for i in s:
    rev=i+rev
print(rev)
if(s==rev):
    print("String Palindrome")
else:
    print("Not a string palindrome")
    
    

   
