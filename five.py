print("1.")
num = 1
while num<=10:
    print("dhruv",",",num)
    num+= 1

print("2.")
i1= 5
while i1>=1:
    print(i1)
    i1-=1

print("3.")
i2=1
while i2<6:
    print(i2)
    if(i2==3):
        break
    i2+=1

print("4.")
i3=0
while i3<6:
    if(i3==3):
        i3+=1
        continue
    print(i3)
    i3+=1

print("5.")
list=[1,2,3,4,5]
for val in list:
    print(val)


print("6.")
seq=range(10)
for i in range(10):  #range(stop)
    print(i)
for i in range(2,10):#range(start,stop)
    print(i)
for i in range(2,10,2):#range(start,stop,step)
    print(i)

print("7.")
for val in range(5):
    pass
