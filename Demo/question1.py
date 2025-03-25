list1 = [{'horsepower': 200, 'torque': 250},
         {'torque': 300, 'displacement': 2},
         {'horsepower': 150, 'cylinders': 4}]

# 1
def listToDict(list):
    dict1 = {}
    for d in list:
        for key,value in d.items():
            if key in dict1:
                val = dict1.get(key)
                val += value
                dict1[key] = val
            else:
                dict1[key] = value
    return dict1

dict1 = listToDict(list1)
print(dict1)           
    
# 2
max_value = 0
ans_key = ''

for key,value in dict1.items():
    if value > max_value:
        ans_key = key
        max_value = value

print(ans_key,' ',max_value)

# 3
count = 0
prefix = 'tor'

for key in dict1.keys():
    if key.startswith(prefix):
        count += 1
    
print(count)

# 4 
min,max = 0,10
res_dict = {}

def keyInRange(min,max):
    for key,value in dict1.items():
        if value >= min and value <= max:
            res_dict[key] = value 

keyInRange(min,max)
print(res_dict)

# 5 
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)


