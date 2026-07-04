str1 = "1.dhruv \n ghodasara."
print(str1)
str2 = "2.ashokbhai \t patel."
print(str2)

#concatenation
str3= "dhruv"
str4= "patel"
print(3,".",str3+str4)
print(3,".",str3+" "+str4)

#lenth of str
print(4,".",len(str1))
print(4,".",len(str3+" "+str4))

#indexing
str="dhruv"
ch1 = str[0]
ch2 = str[1]
print(5,".",ch1)
print(5,".",ch2)
print(5,".",str[3])
print(5,".",str[-1])
print(5,".",str[-3])

#string slicing
str="dhruv is my name"
print(6,".",str[0:2])
print(6,".",str[1:3])
print(6,".",str[ :3])
print(6,".",str[1: ])

#string function
str="dhruv is my name"
print(7,".",str.endswith("d"))
print(7,".",str.endswith("v"))

print(8,".",str.capitalize()) 
# or
# str="dhruv"
# str=str.capitalize()
# print(8,".",str)

print(9,".",str.replace("u","a"))
print(9,".",str.replace("dhruv","master"))

print(19,".",str.find("r"))
print(19,".",str.find("dhruv"))
print(19,".",str.find("z"))

print(20,".",str.count("m"))

#conditional statements

age=int(input("enter your age:"))
if(age>=18):
    print("con. your age is",age,"so you can get voter id card.")
elif(age<=18):
    print("your age is",age,"so you can not get.")

light=input("Enter trafic light:")
if(light=="green"):
    print("you can go")
elif(light=="red"):
    print("stop")
else:
    print("lifht is broken")

#nesting

age=int(input("Enter your age:"))
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("can not drive")

