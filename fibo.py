import sys

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for index, fibonacci_number in enumerate(fib()):
    if index == int(sys.argv[1]):
        print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
        break
