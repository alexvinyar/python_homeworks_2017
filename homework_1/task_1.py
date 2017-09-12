def fibonacci(n):
    minus2 = 0
    minus1 = 1
    for i in range(n):
        s = minus2 + minus1
        minus2 = minus1
        minus1 = s
    return minus2
