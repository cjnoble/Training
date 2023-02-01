

def power (num, p):

    if p == 0:
        return 1

    else:
        return num*power(num, p - 1)


def factorial(num):

    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(power(10, 3))
print(factorial(3))
