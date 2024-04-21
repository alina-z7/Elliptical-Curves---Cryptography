'''
Extended Euclidean Algorithm - Finding Multiplicative Inverse

Input:
-----
a, b = two integers

Output:
-------
t_1 = gcd(a, b)

Comments:
---------

'''

def ex_gcd(a, b):
    assert a == abs(int(a))
    assert b == abs(int(b))

    t_1 = 0
    t_2 = 1
    t = 0

    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        t = t_1 - t_2 * q
        t_1 = t_2
        t_2 = t
    return t_1