# 1

list1 = [1,2,3,4,5]
# while True:
#     num = int(input("Enter an integer (0 to stop) : "))
#     if num == 0:
#         break
#     list.append(num)

def sumOfEven(list):
    sum = 0
    for num in list:
        if num%2 == 0:
            sum += num
    print(sum)
 
sumOfEven(list1)

# 2 

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

def setIntersect(set1,set2):
    set3 = set()
    for i in set1:
        if i in set2:
            set3.add(i)
    return set3

res2 = setIntersect(set1,set2)
print(res2)

# 3

list2 = [1,2,3,4,5]
list3 = [3,4,5,6,7]

def listIntersect(l1,l2):
    res_list = []
    for i in l1:
        if i in res_list:
            continue
        else:
            res_list.append(i)
    for i in l2:
        if i in res_list:
            continue
        else:
            res_list.append(i)
    print(res_list)

listIntersect(list2,list3)

# 4 

tup1 = (10,50,60,25,5)
max = 0

for i in tup1:
    if max < i:
        max = i

print(max)

# 5

list4 = [1,2,3,4,5,2,2]

def removeNumber(num):
    res_list = []
    for i in list4:
        if i == num:
            continue
        else:
            res_list.append(i)
    print(res_list)

removeNumber(2)

# 6

tup1 = (1,2,3)
tup2 = (1,2,3)

def equalTuple(t1,t2):
    if len(tup1) != len(tup2):
        return False
    for i in range(0,len(tup1)):
        if tup1[i] != tup2[i]:
            return False
    return True 

res6 = equalTuple(tup1,tup2)
print(res6)

# 7 
lst = []
# while True:
#     lst1 = []
#     while True:
#         num = int(input("Enter an integer : "))
#         if num <= 0:
#             lst.append(lst1)
#             break
#         else:
#             lst1.append(num)
#     if num < 0:
#         break


def flattenList(lst):
    res_list = []
    for i in range(0,len(lst)):
        for j in range(0,len(lst[i])):
            res_list.append(lst[i][j])
    print(res_list)

print(lst)
flattenList(lst)

# 8 
dict1 = {1:'raj',2:'dev',3:'Gourav'}

def removeKeyValue(k):
    try:
        del dict1[k]
    except Exception as e:
        print(e)

removeKeyValue(2)
print(dict1)

# 9 

dict2 = {'raj':70,'dev':50,'Gourav':60}

def sortByValue(dict2):
    return dict(sorted(dict2.items(), key=lambda item:item[1]))
    # return dict(sorted(dict2.items(), key=lambda item:item[1], reverse = True))

res_dict2 = sortByValue(dict2)
print(res_dict2)

# 10

dict3 = {1:10,2:10,3:10}
dict4 = {2:10,3:10,4:10}

def mergeDict(d1:dict,d2:dict):
    res_dict = {}
    for key,value in d1.items():
        if key in res_dict:
            res_dict[key] += value 
        else:
            res_dict[key] = value
    for key,value in d2.items():
        if key in res_dict:
            res_dict[key] += value
        else:
            res_dict[key] = value
    return res_dict

res_dict = mergeDict(dict3,dict4)
print(res_dict)

# 11 

