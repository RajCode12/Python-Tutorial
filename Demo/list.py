l1=[22,44,9,22,44,10]
print(l1)
for i in l1[0:2]:
    print(i)

l1[2]=100
print(l1)
print(type(l1),'Len=',len(l1))
print(l1[0])
print(l1[2:5]) #2-4
print(l1[-2])
l1.append(77)
l1.append(20)
print(l1)
l1.insert(1,88)
print(l1)
print(l1[::-1])
print(l1)

l2=['ajay','pune','python','mumbai']
l2.reverse()
print(l2)

for index,data in  enumerate(l2):
    print(index,data)

l3=[10,'ajay','pune',True,34.55]
print(l3)


# s1='python'
# s2='python'
# print(id(s1),id(s2))

l4=[10,20,30]
l5=[10,20,30]
l6=l5
print(id(l4),id(l5),id(l6))
l6[0]='yash'
print(l5,l6)

l7=[10,20,'Yash']
l8=l7.copy()
print(id(l7),id(l8))
#l7[0]='Pune'
print(l7,l8)

print(l7 is l8) #compare address
print(l7 is not l8) # True
list9=[22,'Rahul']
print(l7==l8) # compare elements
print(l7==list9)

list1=[22,33,44,7,89,22,10,5]
print(44 in list1)  #check if 44 is present in list or not

list1=[11,22]
list2=[44,66,77,'python',True,99.66,11]
list3=list1+list2
print(list3)

list1=[44,55]
list2=[7,8,9]
list1.extend(list2)
print(list1)

list1=[22,33,44,7,33,22,55,22,33,10]
print(list1.count(22))
print(list1.index(33))
print(list1.index(33,2))
try:
    list1.remove(56)  # remove given element/value
    print(list1)
except ValueError as e:
    print({e})

try:
    list1=[55,66,3,22,4,10]
    print('popped value ',list1.pop()) #pop last element
    print(list1)
except IndexError as e:
    print({e})

list1=[66,55,77,88]
print('popped value ' ,list1.pop(2))#pop element at given index
print(list1)


list1=[ [66,55] , [77,88], [99,22] ]
print(list1[2][0])
a,b,c=list1
print(a,b,c)
print(a,type(a))

l1=[33,'Yash',99.77,True]
a,b,c,d=l1  #unpacking
print(a,b,c,d,type(a),type(b),type(c),type(d))


# for j in range(10,1,-1):
#     print(j)

l1=[x for x in range(1,5)]  #list comprehension
print(l1)

l1=[x for x in range(1,10) if x%2==0]#list comprehension
print(l1)


l1=[x for x in range(1,5) if x%2] #list comprehension
print(l1)


l1=[x*x for x in range(10,0,-1)] #list comprehension
print(l1)

'''
Max and min element of a list
sort list
secound maximum element
merge two list
'''

list1 = [x for x in range(1,10)]

max1 = max(list1)
print(max1)

min1 = min(list1)
print(min1)

sort1 = sorted(list1)
print(sort1)

rev1 = list1[::-1]
print(rev1)


