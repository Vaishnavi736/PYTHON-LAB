#rev a string
s=input("Enter string")
rev=s[::-1]
print("Reverse: ",rev)
#rev without slicing
s=input("Enter string")
rev=""
for i in s:
     rev=i+rev
print("Reverse  : ",rev)    
#string palindrome
s=input("Enter string")
rev=""
for i in s:
    rev=i+rev       
if s==rev:
     print("It's a String Palindrome")
else:
     print("It's not a String Palindrome")   
#length of string
s=input("enter string")
count=0
for i in s:
    count+=1
print("Length of string: ",count)  
#vowel count
s=input("Enter string")
count=0
for i in s:
   if i in "aeiouAEIOU":
       count+=1
print("Vowel count: ",count)       
#vow and con count
s=input("Enter string")
vow,con=0,0
for i in s:
   if i in "aeiouAEIOU":
       vow+=1
   else:
       con+=1    
print("Vowel count: ",vow)       
print("Consonant count: ",con)     
#even length words
s=input("Enter string")
k=s.split()
for i in k:
    if(len(i)%2==0):
        print("Words with even length: ",i)
        
