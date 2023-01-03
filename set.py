#set:collection,unordered and unindexed,no duplicate members
#create set
fruit_set={'apple','orange','mango'}
print(fruit_set)
#check if in set
print('apples'in fruit_set)
#add to set
fruit_set.add('grape')
print(fruit_set)
#remove from set
fruit_set.remove('grape')
#clear set
fruit_set.clear()
print(fruit_set)
#delete set
del fruit_set
print(fruit_set)


#<--------------------------03/01/22------------------------------------>
thisset={"a","b","c","d","e"}
#thisset.clear() #remove all elements from set
set1=thisset.copy()
thisset.add("f")
print(thisset)
print(set1)
#<--------------Actual Set Functions also works in PYthon Sets----------->
# difference ()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #print elements which are in x and not in y
z = y.difference(x) #print elements which are in y and not in x
print(z)
# difference_update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)  #update the original set means now set x has elements which are not in y
print(x)

#discard()

x={"a","b","c","d"}
x.discard("b") #This method is different from the remove() method,
# because the remove() method will raise an error if the
# specified item does not exist, and the discard() method will not.
print(x)

#intersection()
x={"a","b","c","d","e","f"}
y={"e","f","g","h","i","j"}
z=x.intersection(y)
print(z)

#intersection_update()

x={"a","b","c","d","e","f"}
y={"e","f","g","h","i","j"}
x.intersection_update(y) #update the original set means now set x has elements which are present in y also
print(x)

#isdisjoint()

x={1,2,3,4,5,6}
y={6,7,8,9,10}
z={0,3,4,5,2}
print(x.isdisjoint(y)) #set x and y has  a common element 6 so it gives false
print(y.isdisjoint(z)) #set y and z does not have a common element so it will give true

#issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)  #all elements of set a are present in set y so it will give true
print(z)

#issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) #all the elements of set y are present in set x so it will give true
print(z)

#pop ()
fruits = {"orange","apple", "banana", "cherry","kiwi"}
fruits.pop() #it removes the random element from the set
x=fruits.pop() #contains the current removed element
print(x)
print(fruits)

#symmetric_diffrence()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #jo element dono me common h unko hata dega
print(z)

#symmetric_difference_update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  #jo element dono me common h unko hata dega and x wale set me hi updated set hoga

#union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) #combinely dono ko likh dega or common element jo dono me h unko ek bar likhega
print(z)

#update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) #x me combinely x and y ki values dal dega and orginal x me hi yeh changes honge
print(x)

#if we want to remove the duplicate elements from the list then we make set of that list
list1=[1,2,3,2,4,5,6,4,7,7,8,8,5,4,3,8,9]
list2=list(set(list1))
print(list2)