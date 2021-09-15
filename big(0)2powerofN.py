#fibonacci
def fib(num):
    if num==0 or num==1:
        return num
    else:
        return fib(num-1)+fib(num-2)

num=10
for i in range(0,num):
    print(fib(i))