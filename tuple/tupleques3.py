#Python program to create a list of tuples from given list having number and
# its cube in each tuple
a=(1,2,3,4,5)
result = []
for val in a:
    res=[val,val**3]
    res=tuple(res)
    print(res)



