

def euclid_gcd (a, b):

    assert a > b

    while True:

        remainder = a%b

        if remainder == 0:
            return b

        a = b
        b = remainder

print(euclid_gcd(96, 60))
print(euclid_gcd(20, 8))