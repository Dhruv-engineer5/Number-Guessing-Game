print(1,".","hello world.","my name is dhruv")
print(2,".",55)
print(3,".",55+5)
print(3,".",55,"+",5)

name = "dhruv"
age = 17
old = False
price = 15.5
age2 = age
any = None

print(4,".",name)
print(5,".",age)

print(6,".","my name is:", name)
print(7,".","my age is:", age)
print(8,".","my age is:", age2)
print(9,".","I am old:",old)

print(10,".",type(name))
print(11,".",type(age))
print(12,".",type(price))
print(13,".",type(old))
print(14,".",type(any))

a = 5
b = 2
sum = a+b

#arithmetic operators

print(15,".",a + b) #sum
print(16,".",a % b) #remainder
print(17,".",a * b) #multiplication
print(18,".",a / b) #divition 
print(19,".",a - b) #difrection
print(20,".",a ** b) #power,a^b

#relational operators

print(21,".",a == b) #for check a=b
print(22,".",a != b) #for check a not= b, "!"is for not
print(23,".",a > b)
print(24,".",a <= b)

#assignment operators

num = 10
#num = num + 10 , or
num += 10

print(25,".",num)

#logical operators 

print(26,".",not False)
print(27,".",not True)
print(28,".",not (a<b))

val1 = True # and operator
val2 = True
print(29,".", val1 and val2)

val1 = True
val2 = False
print(29,".", val1 and val2)

val1 = False
val2 = False
print(29,".", val1 and val2)

val1 = False  #or operator
val2 = True
print(30,".", val1 or val2)
print(31,".",(a==b) or (a>b))

print(32,".","short cut=ctrl+/") #comment
'''
print(comment)
print(comment)
'''

#type convertion

c = 2 #int
d = 4.25 # flot # flot>int
sum = c + d # flot
print(33,".",sum)

e = "2" #str
d = 4.25 #flot
e = int(e) # for str => int
print(34,".",e + d)

#input                            

# input("how are you:")
# print("good dhruv")
#or
name = "dhruv"
# informetion = int(input("how old are you:"))
informetion = float(input("how old are you:"))
# informetion = str(input("how old are you:"))
print("welcome",name)
print(type(informetion),informetion)

A,B=1,2
C=4
print((A*B)+C)

A,B=1,2.0
C=A//B
print(C,A/B)
