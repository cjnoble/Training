
x = [i for i in range (1, 51)]

# Filters

def is_odd (x):

    if x%2 == 0:
        return False
    else:
        return True

o = list(filter(is_odd, x))
print(o)

# Transforms

def square (x):
    return x**2




s = list(map(square, x))
print(s)