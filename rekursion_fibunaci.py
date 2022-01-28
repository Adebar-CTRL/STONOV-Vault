

def fib_rek(n):
    if n <= 1:
        return 1
    else:
        return fib_rek(n-1)+fib_rek(n-2)
n =int(input("n"))
print(fib_rek(n))