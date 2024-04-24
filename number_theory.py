'''
Euclidean Algorithm - Finding the GCD

Input:
-----
a, b = two integers

Output:
-------
gcd = gcd(a, b)

'''
def gcd(a, b):
    assert a == abs(int(a))
    assert b == abs(int(b))

    while b != 0:
        r = a % b
        a = b
        b = r
    return a

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
    return t_1, a

def mod_inv(a, N):
    # 3 * _(7)_  = 1 (mod 5)
    # 9 * _(4)_ = 1 (mod 7)
    # a * a^-1 = 1 (mod N)
    for i in range(2, N):
       if gcd(a, i) == 1:
           return i
    return None

print(mod_inv(3, 5))
print(mod_inv(9, 7))