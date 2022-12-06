#tuple:ordered,unchangable,allows duplicate members
fruit_tuple=('apple','orange','mango')
#using constructor
#fruit_tuple=tuple(('apple','orange','mango'))
#get single value
print(fruit_tuple[1])
#can not change value
#fruit_tuple[1]='grape'#gives error because unchangable
#tuples withn one value should have trailing comma
fruit_tuple_2=('apple',)
#get length of tuple
print(len(fruit_tuple))
del fruit_tuple_2
print(fruit_tuple)