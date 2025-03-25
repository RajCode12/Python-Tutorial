# 1

def removeVowels(s):
    res = ''
    for char in s:
        if char in "aeiouAEIOU":
            continue
        else:
            res += char
    return res

res1 = removeVowels('raAj')
print(res1)

# 2 

def countDigits(num:int):
    count = 0
    if num < 0:
        num *= -1
    elif num == 0:
        return count
    while num > 0:
        count += 1
        num //= 10
    return count

res2 = countDigits(38430)
print(res2)

# 3 

def replaceSubstring(s,s1,s2):
    return s.replace(s1,s2)

res3 = replaceSubstring("Rajrajraj","aj",' ')
print(res3)
        
# 4

def factorial(num):
    fact = 1
    if num < 0:
        return -1
    elif num <= 1:
        return fact
    for i in range(2,num+1):
        fact *= i
    return fact
    
res4 = factorial(5)
print(res4)

# 5

def sumOfOddDigits(num):
    sum = 0
    if num < 0:
        num *= -1
    elif num == 0:
        return sum
    while num > 0:
        rem = num%10 
        if rem%2:
            sum += rem 
        num //= 10
    return sum 

res5 = sumOfOddDigits(12345)
print(res5)

# 6 

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True


def primeFactor(num):
    for i in range(2,num):
        if isPrime(i) and num % i == 0:
            print(i,end=' ')
    print()

primeFactor(15)

# 7 

def isSubstring(s1,s2):
    if s1 in s2:
        return True
    return False

res7 = isSubstring('aj',"Raaj")
print(res7)

# 8 

class DigitNotFoundException(Exception):
    def __init__(self,message):
        super().__init__(message)

def isDigitFound(num):
    count = 0
    if num < 0:
        num *= -1
    while num > 0:
        if num%10 == 7:
            count += 1
        num //= 10
    if count == 0:
        raise DigitNotFoundException("Digit 7 Not Found...")
    else:
        print(count)

try:
    isDigitFound(171765)
    isDigitFound(12345)
except Exception as e:
    print(e)

# 9 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

res9 = gcd(12,15)
print(res9)

# 10 

s1 = "Rajrajraj"
s2 = s1.replace('aj','')
print(s2)




