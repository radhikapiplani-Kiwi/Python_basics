def ispalindrome(v):
    save=str(v)
    reverse=str(v)[::-1]
    if save==reverse:
        return True
lis=[1,55,88,19,44,303,8998,6776,45677654,308,9678,234432]
list1=[]
for i in lis:
    value=int(i)
    if ispalindrome(value)==True:
        list1.append(value)
print(list1)