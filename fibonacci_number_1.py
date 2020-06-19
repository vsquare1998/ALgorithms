# Uses python3
def calc_fib(n):
    lis = [0,1]
    
    for i in range(2,n+1):
        lis.append(lis[-1]+lis[-2])
    return lis[-1]

n = int(input())
print(calc_fib(n))
