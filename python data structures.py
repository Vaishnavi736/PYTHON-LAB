#LIST OPERATIONS
l1=[]
n=int(input("enter no of elements: "))
for i in range(n):
     ele=int(input())
     l1.append(ele)
print(l1) 
l2=[]
n=int(input("enter no of elements: "))
for i in range(n):
     ele=int(input())
     l2.append(ele)
print(l2)   
print(l1+l2)
print(l1*3)
print(l1[3])
print(l1[1:4:1])
print(4 in l2)
print(4 not in l2)
for i in l1:
    print(i)
