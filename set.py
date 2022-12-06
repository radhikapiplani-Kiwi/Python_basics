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