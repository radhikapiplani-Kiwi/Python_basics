#sum of tuple elements
t=(30,20,45,67,89,28)
count=0
for val in t:
    count=count+val
print(count)
#palindrome number
t1=(45,67,89,55,44,88,909,202,303)
for i in t1:
    if str(i) == str(i)[::-1]:
        print(i,end=" ")
#reverse a number
num=8909
print(str(num)[::-1])
#modulo of two tuples
from operator import mod
tuple1=(14,2,3,4,5)
tuple2=(6,7,8,9,10)
result=tuple(map(mod,tuple1,tuple2))
print(result)
tup=(90,80,67,45,34)
for i in tup:
    print((i))
a=(78,56,34,67,55,28,90)
ab=[]
for x in a:
   m=str(x)
   b="".join(m)
   ab.append(b)
print(ab)
