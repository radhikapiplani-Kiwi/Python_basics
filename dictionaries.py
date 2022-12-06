#dictionary:unordered,unchangable,indexed,no duplicate members
person={'first_name':'john',
         'last_name':'doe',
         'age':30}
#using constructor
#person=dict(first_name='john',last_name='doe',age=30)

#access value
print(person['first_name'])
print(person)
print(person.get('last_name'))
#add key /value
person['phone']='345-678-098'
#get keys
print(person.keys())
#get values
print(person.items())
#make copy
person2=person.copy()
person2['city']='boston'
print(person2)
print(person)
del(person['age'])
print(person)
person.pop('phone')
print(person)
#clear
person.clear()
#get length
print(len(person2))
#list of dict
people=[{'name':'martha','age':40},{'name':'bob','age':20}]
print(people)
print(people[1]['name'])