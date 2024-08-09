#SUMAVG
l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter elements: "))
    l.append(ele)
print(l) 
print("sum: ",sum(l),"avg: ",sum(l)/len(l))
#INTERCHANGING
l=[]
n=int(input("Enter no of ele: "))
for i in range(n):
    ele=int(input("Enter the element"))
    l.append(ele)
print(l)
a=int(input("Enter the first index"))
b=int(input("Enter the second index"))
temp=l[a]
l[a]=l[b]
l[b]=temp
print("After interchanging: ",l)
#DELETING FIRST OCCURENCE
l=[]
n=int(input("Enter the no of elements "))
for i in range(n):
    ele=int(input("Enter the element"))
    ele=l.append(ele)
print(l)
d=int(input("Enter element to be removed: "))
l.remove(d)
print(l)
#EVEN ODD
l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter elements: "))
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
#minandmax
l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter elements: "))
    l.append(ele)
print(l) 
print(max(l))
print(min(l))
#
l1=[]
l2=[]
n=int(input("Enter the no of elements "))
print("Enter elements in list1")
for i in range(n):
    ele=input("Enter the element")
    ele=l.append(ele)
print(l1)
print("Enter elements in list2")
for i in range(n):
    ele=input("Enter the element")
    ele=l.append(ele)
print(l2)
#reverse without using reverse() 
l=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    ele=int(input("Enter elements: "))
    l.append(ele)
print(l) 
i=1
for i in range(n//2):
    temp=l[i]
    l[i]=l[n-i-1]
    l[n-i-1]=temp
print(l)  
