A=int(input("Enter your number:"))
B=int(input("Enter your number:"))
C=int(input("Enter your number:"))

list=[A,B,C]

copy=list.copy()
copy.reverse()

if(copy==list):
    print("your lost is phelindrom")
else:
    print("your lost is not phelindrom")
