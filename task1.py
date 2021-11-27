import math

def evaluate (x, a):
    res = 0
    for i in range (len(a)):
        res += a[i]*(x**i)
    return (res)

def exp (x, n):
    a = []
    for i in range (0, n):
        a.append(1/math.factorial(i))
    return (evaluate(x, a))

tests = [0.001, 0.01, 0.1, 1, 10, 30, 100]
for test in tests:
    print ("exp = ", exp(test, 150), "math.exp = ", math.exp(test), "\n")
