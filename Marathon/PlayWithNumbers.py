# count digits of a number
def countDigits(num):
    count = 0
    while num > 0:
        count += 1 
        num //= 10 
    return count

# print table of a number
def printTable(num):
    for i in range(1,11):
        print(i*num, end = ' ')
    print()

# check if a number is prime or not
def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# print prime factors of a number
def primeFactors(num):
    i = 2
    lst = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            lst.append(i)
    if num > 1:
        lst.append(num)
    return lst

# print binary representation of a number
def binaryRepresentation(num):
    lst = []
    while num > 0:
        d = num%2
        lst.append(str(d))
        num //= 2
    lst = lst[::-1]
    return ''.join(lst)

def reverseNumber(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10
    return rev

# calculate sum of digits of a number
def sumOfDigits(num):
    sum = 0
    while num > 0:
        sum += (num % 10)
        num //= 10
    return sum

def puzzleAdv():
    # taking input from user
    while True:
        try:
            num = int(input("Enter an integer : "))
            if num > 0:
                break
            else: 
                print("Please enter a positive integer : ")
        except ValueError as e:
            print(e)
    
    # output based on the digit count of input
    digits = countDigits(num)
    if digits == 1:
        printTable(num)
    elif digits == 2:
        print("Is Prime : ", isPrime(num))
        print("Prime Factors : ", primeFactors(num))
        print("Binary Representation : ", binaryRepresentation(num))
    elif digits == 3:
        print("Reversed number : ", reverseNumber(num))
    else:
        print("Result : ", num%sumOfDigits(num))
    
# calling the function
puzzleAdv()
        
    
    
        
    
