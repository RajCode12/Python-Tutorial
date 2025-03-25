
f = open("info1.txt","w")
f.write("hello world")
f.close()

f = open("info1.txt", "a")
f.write(" thank you ")
f.close()

#open and read the file after write
f = open("info1.txt", "r")
print(f.read())

#Create a file called "myfile.txt":
#"x" - Create - will create a file, returns an error if the file exists
#f = open("info1.txt", "x")
#f.close()


#\n ---- \r\n 
#list of strings
list1=["thank you welcome good day\n","hi\n","good night\n"]
f = open("info2.txt","w")
f.writelines(list1)
f.close()

f=open("info2.txt","r")
lines= f.readlines()
print('---',lines)
f.close()

#f = open("info6.txt", "r")
#print(f.read())

f=open("info2.txt","r")
for x in f:
  print(x)
f.close()


# read line ny line
f=open("info2.txt","r")
print("current position of file pointer ",f.tell())
line1=f.readline()
print("current position of file pointer ",f.tell())
line2=f.readline()
print("current position of file pointer ",f.tell())
line3=f.readline()
print("current position of file pointer ",f.tell())

'''print(line1)
print(line2)
print(line3)'''

f.close()

#to find current location of file pointer
f=open("info2.txt","r")
print('position of file pointer ',f.tell())  #0
str = f.read()
#print(str)
print('position of file pointer ',f.tell())
f.close()

# to move file pointer to specific position
f=open("info2.txt","r")
f.seek(5,0) # (offset-howmanybytestomove,fromwheretostart)
print("file data =",f.read())
f.close()


f = open("info.txt","w")
f.write("welcome to python coding")
f.close()

import os
print("current working directory= ",os.getcwd())
#os.rename("info.txt","data.txt")
#os.remove("data.txt")


with open("info2.txt", "rb") as file:
  print("First read:", file.read(5))
  file.seek(2, 1)  # Skip next 2 bytes
  print("After seek:", file.read(5))

