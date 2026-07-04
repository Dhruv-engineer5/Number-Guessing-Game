# Dictionary         

info={
    "Name": "dhruv",
    "age": 17,
    "adult":False,
    "sub":["python","html","java"], 
    12: "std"
}
# info["Name"]="ashok"   #mutablr
print(1,".",type(info))
print(2,".",info)
print(3,".",info["Name"])

# null={}
# null["name"]="dhruv"
# print(null)

#nested

student={
    "name": "dhruv",
    "subject":{
        "maths": 94,
        "physics": 93,
        "chemistry": 96,
        "sansrit": 96,
        "english": 75,
    }
}
print(4,".",student["subject"]["physics"])

#function

print(5,".",student.keys())
print(5,".",list(student.keys()))
print(5,".",len(student.keys()))

print(6,".",student.values())

print(7,".",student.items())
abc=list(student.items())
print(7,".",abc[0])

print(8,".",student.get("name"))
# print(8,".",student.get("name2"))  #none
# print(8,".",student["name2"])  #error

student.update({"age":17})
print(9,".",student)


#sets       #mutable    #set's value immutable

set1={1,2,3,4,5,6,"dhruv"}
print(10,".",set)
print(10,".",type(set))
set2=set()
print(10,".",type(set2))

#function

set1.add(7)
# set1.add([8,9,0])
print(11,".",set1)

set1.remove(7)
print(12,".",set1)

set1.clear()
print(13,".",set1)

set1={1,2,3,4,5,6,"dhruv"}
print(14,".",set1.pop())

set1={1,2,3,4,5,6,7,8,"dhruv"}
set3={7,8,9,0,"ashok"}
print(15,".",set1.union(set3))

print(16,".",set1.intersection(set3))

