dict={"name":"radhika",
"age":22,
"roll no":34,
"stack":"python"}
for x in dict.values():
  print(x,end=" ")
for y in dict.keys():
  print(y,end=" ")
for key,value in dict.items():
    print(key,value)
sort=sorted(dict.items())
print(sort)
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
  dic4.update(d)
print(dic4)
