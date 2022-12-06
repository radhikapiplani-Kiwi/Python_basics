#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#You can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If
if a > b: print("a is greater than b")
#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")
#One line if else statement, with 3 conditions:
