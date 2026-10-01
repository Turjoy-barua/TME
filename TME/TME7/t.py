def lgr(s):
    if s == '':
        return 0
    return 1+ lgr(s[1:])

def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))



