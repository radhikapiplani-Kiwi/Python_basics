'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''
def hi():
  print("Hello from a function")
hi()
#arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#two arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
'''If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
'''You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''If the number of keyword arguments is unknown, add a double ** before the parameter name:'''
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
'''function definitions cannot be empty, but if you for some reason have 
a function definition with no content, 
put in the pass statement to avoid getting an error.'''
def myfunction():
  pass
#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)