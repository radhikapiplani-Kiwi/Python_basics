#iterating over list

list1=["a","b","c","d","e","f"]
for item in list1:
    print(item ,end=" ")
print("")

#iterating over tuple

tup=("a","b","c","d","e","f")
for item in tup:
    print(item,end=" ")
print("")
#iterating list of list

list2=[["a",1],["b",2],["c",3],["d",4],["e",5]]
dict=dict(list2) #converting it into a dictionary
print(dict)
for i,j in list2:
    print(i,j)
#access as dictionary now

print("<---------access as dictionary now------->")
for i,j in dict.items():
    print(i,j)
#print only item in dictionary

print("<---------print only item in dictionary----->")
for i in dict:
    print(i,end=" ")
print("")
#question-------------->
list2=[int,float,"radhika",9,90,0.9,78,7.9,6,34,56,78,38,92,6]
for item in list2:
    if str(item).isnumeric() and item >=6:
        print(item)