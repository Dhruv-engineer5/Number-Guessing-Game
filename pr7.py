marks= int(input("Enter your marks:"))
if(marks>=90):
    print("grade=A")
elif(90>marks>=80):
    print("grade=B")
elif(60<=marks and marks<80):
    print("grade=C")
elif(60>marks>=33):
    print("grade=B")
else:
    print("you are fall")