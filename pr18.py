num = [1,2,3,4,5,6]
name = ["dhruv","daxa","ashok"]

def len_list(list):
    print(len(list))
len_list(num)
len_list(name)

def ali_list(list):
    for val in list:
        print(val, end=" ")
ali_list(num)

def ali_list(list):
    i=0
    while i<len(list):
        print(list[i],end=" ")
        i+=1
ali_list(num)


def fact_n(n):
    i=1
    f=1
    while i<=n:
        f*=i
        i+=1
    print(f)
fact_n(5)


def con_usd(n):
    print(n*90)
con_usd(5)

def num(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")
num(6)
