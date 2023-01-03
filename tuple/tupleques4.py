# Adding tuple to list
t=(1,2,3,4,5)
l=[6,7,8,9,10]
l+=t
print(l)
# Adding list to tuple
t1=(67,90,89,45)
l1=[95,76,80,34]
result=tuple(list(t1)+l1)
print(result)