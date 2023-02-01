import timeit

def even_b (n):
    return bin(n)[-1] != "1"

def even (n):
    return n%2 == 0

def even_a (n):
    return not bool(n & 1)

def test_even_b ():
    i = 1000001
    even_b(i)

def test_even ():
    i = 1000001
    even(i)

def test_even_a():
    i = 1000001
    even_a(i)

#print(even_a(11))

print(timeit.timeit("test_even_b()", globals=locals(), number=1000000))
print(timeit.timeit("test_even()", globals=locals(), number=1000000))
print(timeit.timeit("test_even_a()", globals=locals(), number=1000000))
