dict={"name":"radhika",
      "age":"22",
      "stack":"python"
}
print(dict)
print(len(dict))
print(type(dict))
print(dict["name"])
print(dict.get("name"))
print(dict.keys())
print(dict.values())
if "nam" in dict:
    print("yes exist")
else:
    print("not present")
dict["name"]="abc" #updating the value
print(dict)
dict["year"]=2022 #Adding value to the dictionary
print(dict)
dict.update({"color": "red"})#Second method of adding value to the dictionary
print(dict)
dict.pop("name") #remove any key value pair in the dictionary
print(dict)

#<--------------------------02/01/22------------------------------------>

mydict={"Radhika":"chilli","kareena":"Pizza","Mudit":"pizza","shubham":{"a":"b","c":"d","e":"f"}}
print(type(mydict))
print(mydict)
print(mydict["Radhika"]) #we can use get function also for same
print(mydict.get("Radhika"))
print(mydict["shubham"]["e"])
mydict["Richa"]="junk food" #value added in dictionary
mydict.update({"leena":"toffee"})  #alternate to value added in dictionary
copiedict=mydict.copy()  #copied wale me delete nahi hui value because vo alag khi copied leke padha h
d1=mydict                #d1 is just a pointer like mydict jaise change hoga d1 change hota rhega
del mydict["kareena"]  #deleting
print(copiedict)
print(mydict)
print(d1)
print(mydict.keys())
print(mydict.values())