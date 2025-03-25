#control structures

# check max of 3 numbers
a,b,c=20,30,40
if a>b and a>c:
    print(' a is max')
elif b>c:
    print(' b is max')
else:
    print(' c is max')

# max of 2 numbers
print('a is max' if a>b else 'b is max')

a,b,c=0,4,30
if a>b and a<c:
    print('Hi')
else:
    print('bye')
    

'''a,b=10,20
if a>b:
    break
else:
    print('Done')'''


# check given character is vowel or not
ch='K'
if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print('vowel ')
else:
    print("not vowel")
    
s1='AEIOUaeiou'
if ch in s1:
    print('vowel ')
else:
    print('not vowel')
    
ch='A'
listvowel=['a','e','i','o','u','A','E','I','O','U']
if ch in listvowel:
    print('vowel ')
else:
    print('not vowel')   


# character not vowel
ch='A'
if ch not in s1:
    print('vowel ')
else:
    print('not vowel')
    
ch='E'
if ch!='A' and ch!='E' and ch!='I' and ch!='O' and ch!='U':
    print('not vowel ')
else:
    print("vowel")
    
# profit/loss 
# even/ odd
# +ve/ -ve

# Loops - while , for
'''
calculate sum of digits of a 3 digit number 
n=754

d3=n%10    #  754%10=4
sum+=d3    #  0+4=4
n=n//10    # 754//10 = 75

d2=n%10    # 75%10=5
sum+=d2    #  4+5=
n=n//10    # 75//10=7

d1=n%10    #  7%10=7
sum+=d1    #  9+7=16
n=n//10    #  7//10=0
'''

# while loop 
# calculate sum of numbers from 1 - 10
j=1
sumnumbers=0
while j<=10:
    sumnumbers+=j
    j+=1
    
print('sum of numbers from 1 -10 ',sumnumbers)

# sum of first 5 odd numbers [1,3,5,7,9]=25
# [1,2,3,4,5,6,7,8,9,10......]
sum = 0
maxcnt=5
j=1 
cnt=1
while cnt<=maxcnt:  
  if j%2:
    sum+=j
    cnt+=1
  j+=2
print(sum)

# sum of first 5 even numbers [2,4,6,8,10]=30

sum = 0
maxcnt=5
j=2
cnt=1
while cnt<=maxcnt:  
  if j%2 ==0:
    sum+=j
    cnt+=1
  j+=2
print(sum)

# sum of even numbers in given range [eg: find sum of even numbers between 10-40]
# reverse the number
# calculate sum of digits if a number
# check number is palindrome or not
# calculate factorial of a number eg: 5!=5*4*3*2*1
# print fibonacii series:  0   1   2   3   5  8  13
















