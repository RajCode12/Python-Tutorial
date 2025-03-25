def makecube(n):
    print(n*n*n)
    
makecube(5)
makecube(6)

# 7   [2,3,4,5,6]
# 15  [2,3, STOP loop]
def checkPrime(n):
    flag=True  #consider that number is prime
    for j in range(2,n):
        if n%j==0:
            flag=False  # indicates it is not prime
            break   #come out of loop
    print('Prime' if flag else 'Not Prime')
    
checkPrime(7)
checkPrime(15)
checkPrime(44)
checkPrime(11)

def display(age,city,personname):
    print('age =',age,'city=',city,'person name=',personname)
    
display(32,'Delhi','John')
#display('John',32,'Delhi')

#keyword argument
display( personname='John',age=32,city='Delhi')

display(32,personname='Jay',city='Delhi')

#display(personname='Jay',city='Delhi',32)  #error


#default argument
def add(a,b=6,c=4,d=0):
    print(a,b,c,d)
    
add(4)  #4,6,4,0
add(2,3)  #2,3,4,0
add(10,c=20)# 10,6,20,0

def show(*values):
    for i in values:
        print(i)
    #print(values)

show(1,2,3)
show(1,2,3,5)
show(1,2,3,6,7,8,9,11,22,34,66)

i=10  #global variable

def outerfun():
    i=10     #local variable
    def innerfun():
        i=20
        j=30
        print('inner function values ',i,j)
        print('End of inner function')
    innerfun()
    print('outer function values ',i)

outerfun()



def outerfun():
    contactperson='Ajay'     #local variable
    def showdata():
        #contactperson='Tarun'  # local variable
        print('inner function values ',contactperson)
        print('End of inner function')
    showdata()
    def changeContactPerson(pname):
        nonlocal contactperson
        contactperson=pname
    changeContactPerson('Yash')
    print('contact person ',contactperson)

outerfun()


k=10  #global variable
def magic():
    k=20
    print(k, globals()['k'] )

magic()










    
    
         
            
    
