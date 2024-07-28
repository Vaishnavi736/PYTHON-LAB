//multiplication table
//using for loop
m=int(input("enter which table you want"))
n=int(input("enter the number of steps"))
for i in range(1,n+1):
     print(m,"x",i,"=",m*i)
//using while loop
m=int(input("enter which table you want"))
n=int(input("enter the number of steps"))
i=1
while i<=n:
     print(m,"x",i,"=",m*i)
i+=1
//sum of 10 numbers
//for loop
sum=0
for i in range(1,11):
    sum=sum+i
print("sum of first 10 natural numbers= ",sum)    
//while loop
i=1
sum=0
while i<11:
   sum=sum+i
   i+=1
print("sum of first 10 natural numbers= ",sum)   
//string length and characters
s=input("enter string")
count=0
for i in s:
   print(i)
   count+=1
print("stringlength= ",count)
//factorial
//for loop
n=int(input("enter number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of given number= ",fact)       
//while loop
n=int(input("enter number"))
i=1
fact=1
while i<n+1:
   fact=fact*i
   i+=1
print("The factorial of given number is: ",fact)
//prime
n=int(input("enter number"))
count=0
for i in range(1,n+1):
   if(n%i==0):
       count+=1
if(count==2):
  print("prime")
else:
  print("not a prime")           
//sum of digits
n=int(input("enter number"))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("Sum of digits= ",sum)    
//rev
n=int(input())
temp=n
sum=0
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
print(sum)
//palindrome
n=int(input())
temp=n
sum=0
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if(sum==temp):
   print("palindrome")
else:
   print("not a palindrome")
# Armstrong
n=int(input())
temp=n
sum=0
while n>0:
    rem=n%10
    sum=sum+(rem**3) 
    n=n//10
if(sum==temp):
   print("Armstrong")
else:
   print("not a Armstrong")
     
