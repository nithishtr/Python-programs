x=int(input("enter the number of series to be printed"))
fib1=0
fib2=1
num=2
if x==0:
    print(fib1)
elif x==1:
    print(fib1,fib2)
else:
    print(fib1)
    print(fib2)
    while num<x:
        fib=fib1+fib2
        print(fib)
        fib1=fib2
        fib2=fib
        num=num+1
    
        

    


    