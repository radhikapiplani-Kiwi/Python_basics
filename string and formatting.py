name='radhika'
age=21
print('Hello I am'+name+'and I am'+str(age))
#arguments by position
print('{}{}{}'.format('a','b','c'))
print('{1}{2}{0}'.format('a','b','c'))
#arguments by name
print('my name is {name} and I am {age}'.format(name='radhika',age='21'))
#or
print('my name is {name} and I am {age}'.format(name=name,age=age))
#f-strings(only in 3.6+)
print(f'My name is {name} and I am {age}')
#string methods
s='hello there world'
#capitalize first word
print(s.capitalize())
#make all uppercase
print(s.upper())
#make all lower case
print(s.lower())
#swapcase
print(s.swapcase())
#get length
print(len(s))
#replace
print(s.replace('r','e'))
#count
sub='h'
print(s.count(sub))
#starts with
print(s.startswith('hello'))
#ends with
print(s.endswith('d'))
#splits into a list
print(s.split())
#find position
print(s.find('r'))
#is all alphanumeric
print(s.isalnum())#is all aphabetic
print(s.isalpha())
#is all numeric
print(s.isnumeric())

