def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_loop(n):
    n1, n2 = 0, 1
    
    for i in range(n):
        temp = n2
        print(n1, end='\t')
        n1, n2 = temp, n1 + n2


fib_loop(10)



for i in range(1, 10):
    print(i, ":", fib(i))