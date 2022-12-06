#list:ordered,changable ,allows duplicate members
#create list
numbers=[1,2,3,4,5]
#using a constructor
numbers=list((1,2,3,4,5))
print(numbers)
fruits=['Apples','oranges','grapes','pears']
print(fruits)
#get value
print(fruits[1])
#get length
print(len(fruits))
#append to list
fruits.append ('mangoes')
print(fruits)
#remove from list
fruits.remove('grapes')
print(fruits)
#insert into position
fruits.insert(2,'strawberry')
print(fruits)
#remove from position
fruits.pop(3)
print(fruits)
#reverse list
fruits.reverse()
print(fruits)
#sort list
fruits.sort()
print(fruits)
#reverse sort
fruits.sort(reverse=True)
print(fruits)