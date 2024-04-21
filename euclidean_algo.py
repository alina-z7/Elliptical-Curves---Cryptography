'''
Euclidean Algorithm - Finding the GCD

Input:
-----
a, b = two integers

Output:
-------
gcd = gcd(a, b)

Comments:
---------

'''
def gcd(a, b):
    assert a == abs(int(a))
    assert b == abs(int(b))

    while b != 0:
        r = a % b
        a = b
        b = r
    return a