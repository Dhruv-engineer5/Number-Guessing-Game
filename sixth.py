#function definition 
def cal_sum(a,b):  #parameters
    sum=a+b
    print(sum)
cal_sum(3,6) #function call, arguments
cal_sum(4,9)


def hello():
     print("hello")
hello()


def sum(a=1,b=3):
    print(a+b)
# sum(): jo parameter ma sum(a,b) to output error pan jo parameter ma a=any b=any to :
sum()
sum(2,5)

# recursive fuction
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(5))

def sum_n(n):
    if(n==1):
        return 1
    return sum_n(n-1)+ n
print(sum_n(5))


num = [1,2,3,4,5,6]

def show(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    show(list,idx+1)
show(num)