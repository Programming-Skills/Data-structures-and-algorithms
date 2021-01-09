# Recursion.py

# Recursion = a way of solving a problem by having a function call itself.

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)

# How recursion works?
# 1. A method calls itself 
# 2. Exit from the infinite loop 

def recursionMethod(parameters):
    if exit from condition satified:
        return some value
    else:
        recursionMethod(modified parameters)

def recursiveMethod(n):
    if n<1:
        print("n is less than one")
    else:
        recursionMethod(n-1)
        print(n)

# Recursive

def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

# Iterative

def powerOfTwo(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power

# How to write recursion in 3 steps?

# 1. Recursive case - the flow

# n! = n * (n-1) * (n-2) * ... * 2 * 1 -> n! = n * (n-1)!

# 2. Base case - the stopping criterion

# 0! = 1
# 1! = 1

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)

# 3. The unintentional case - the constraint

### Fibonacci numbers - recursion ###

# 1. Recursive case - the flow

def fib(n):
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2) 