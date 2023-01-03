#maximum and minimum k elements in a tuple
a=(3, 7, 1, 18, 9)
print(len(a))
print(a.__sizeof__())
print(sorted(a))
k=2
result=[]
a=sorted(a) #sort the tuple
for i,val in enumerate(a):
    if i<k or i>=len(a)-k:
        result.append(val)
result=tuple(result)
print(result)


