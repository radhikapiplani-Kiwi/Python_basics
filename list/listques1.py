# #reverse a list
# l=[1,2,3,89,67,4,5,6,90]
# count=0
# for val in l:
#     count=count+1
# print(count)
# size=len(l)
# temp=l[0]
# l[0]=l[size-1]
# l[size-1]=temp
# print(l)
# #swap two elemets in a list
# l1=[7,8,9,4,3,5]
# pos1=0
# pos2=4
# temp=l1[pos1]
# l1[pos1]=l1[pos2]
# l1[pos2]=temp
# print(l1)
# # swap elements in string list
# str_list=["hello" "i" "am" "radhika" "piplani"]
# res = [sub.replace('am', 'i') for sub in str_list]
# print(str(res))
# # python code to Check if element exists in list or not
#
# l2=[ 1, 6, 33, 5, 3, 43 ]
# l2.insert(2,78)
# l2.pop(2) #pop remove lement from specified index
# l2.remove(5) #remove element=5 from this list
# print(l2)
# i=5
# if i in l2:
# 	print("exist")
# else:
# 	print("not exist")
# #reverse a list
# l3=[4,3,5,6,7,9,8,8,8,8,9,8,9,9,6,7,4]
# rev=l3[ : :-1]
# print(rev)
# #count occurance of any element
# count=0
# element=8
# for val in l3:
#    if val==element:
#        count=count+1
# print(count)
# lis=[76,56,45,36,90]
# for j in lis:
#     print(j)
# #python program for sum pair
# a=[2, 1, 5, 7, -1, 4]
# sum=6
# i=0
# j=i+1
# count=0
# for i in a:
#     for j in a:
#         if i+j==sum:
#          count=count+1
# print(count)
# v=1221
# save=str(v)
# reverse=str(v)[::-1]
# if save==reverse:
#   print("true")
# lis=[1,4,5,6,7,8,90,98,67]
# for i in lis:
#    print(i)
# list1=[0,1,3,4,5,6,7,8,9]
# print(list1[::-2])
# print(list1[3:-3])
# x=list(range(-5,3,3))  #it works as [-5,-4,-3,-2,-1,0,1,2,3] it will give -5 and leave 2 element and give -2
# print(x)
#<--------------------filter function ------------->
# list=[[]]*3
# list[1].append(5)
# print(list)
list=[i**2 for i in range(2,4)]
print(list)