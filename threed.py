#list in python
marks1= [90.9,99,98.9,99,97.7,88.8,86.8]
print(1,".",marks1[0])
# marks[1]=80      #list is mutable        #aa string and tuples ma na thay 
print(2,".",marks1[1])
print(3,".",len(marks1))
print(4,".",marks1)
print(5,".",type(marks1))

#list slicing
marks1= [90.9,99,98.9,99,97.7,88.8,86.8]
print(6,".",marks1[1:2])

#list functions
marks1= [90.9,99,98.9,99,97.7,88.8,86.8]

marks1.append(80)
# print(7,".",marks.append(80))
print(7,".",marks1)

# marks.sort()          #ascending order 123...
marks1.sort(reverse=True)   #descending order 321..
print(8,".",marks1)

# marks.reverse()
# print(9,".",marks)

marks1.insert(0,"dhruv")
print(10,".",marks1)

marks1.remove(99)
print(11,".",marks1)

marks1.pop(2)
print(12,".",marks1)


#tuples               #tuples is immutable
marks2=(2,3,6,1,7,1)          #marks2=() => emty tuple
print(13,".",type(marks2))
print(14,".",marks2[0])
print(14,".",marks2[1])

print(15,".",marks2[2:4])

print(16,".",marks2.index(1))

print(17,".",marks2.count(1))


