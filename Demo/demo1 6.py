#I am single line comment

'''
Multi line comment
'''

a=10
b=20.6
c=True
d=False
s1='Python'
print(a,b,c,d,s1)
print(a,b,c,d,s1,sep='**')

n1,n2,n3,n4=10,300.5,True,'Pune'
print(n1,n2,n3,n4)
print(type(n1),type(n2),type(n3),type(n4))

print('hello',end=' ')
print('world')
print('welcome')

print(10+4) #14
print(3+5.6)
print(3+True)
print(3+False)
print(3.5+True)
print(3.5+False)
print('hi'+'hello')
print('10'+'20') #1020
print('hello'+'2') #hello2
#print('hello'+2)  # error
#print('hello'+2.5) #error


a,b=10,10
if a>b:
    print('a is max')
elif b>a:
    print('b is max')
else:
    print('both are same')

    
print('end ')

# +ve / -ve / zero
# profit/loss  -- salesvalue & purchase value
# even or odd

a=10
if a>0:
    print('+ve number ')
elif a<0:
    print('-ve number')
else:
    print('zero')
    
salesvalue,purchasevalue=3000,5000
if salesvalue>purchasevalue:
    print('profit')
elif salesvalue<purchasevalue:
    print('Loss')
else:
    print('No profit no loss')
    
a=21
if a%2:
    print('Odd')
else:
    print('even')
    
'''
a=21
if a%2==0:
    print('Even')
else:
    print('odd')
''' 
print('Odd' if a%2 else 'Even')

# max of 3 numbers  --- and

print(11/2)
print(11//2)  #check this operator with float values

print(2**5) # 2*2*2*2*2

n=10
N=20
#1num=20  # error
num1=30 #valid
annual_salary=300000
_salary=40000
#salary$=30000  #error

# Loops and functions

s1='hello world'
print(s1)
print(s1[0])
print(s1[-1])

# slicing   [startindex : endindex : stepvalue ]

print(s1[0:7:2])  # 0-6
print(s1[0:7:3])  # 0-6
print(s1[2:])
print(s1[:8])
print(s1[:])
print(s1[::])
print(s1[-5:-1])
print(s1[-5:-1:2])

# range function 
#  while loop
# for loop
































