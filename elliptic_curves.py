import math
import random

'''
Elliptical Curve Addition Algorithm - Finding Third Point R' on Common Curve E

Input:
-----
P, Q = points on an elliptic curve E
A = coefficient of the equation E: y^2 = x^3 + Ax + B

Output:
-------
R' = the additive result of P (+) Q
'''

def elliptic_curve_addition(P, Q, E):
    O = (float('inf'), 0) # ideal point

    if P == O: # if L is a vertical line and P is a point on L, return Q
                # i.e P + Q = Q if P = O
        return Q 
    
    if Q == O: # if Q is a point on a vertical line L 
                #  # i.e P + Q = Q if Q = O
        return P
    
    # else retrieve the coordinates from P and Q
    x1, y1 = P 
    x2, y2 = Q

    # check if P and Q are reflective points across the vertical line L,
    # then return the ideal point, since we can't calculate the third point with undefined slope 
    if x1 == x2 and y1 == -y2:
        return O

    # if P and Q are not the same point
    if P != Q:
        # calculate the slope of the vertical line L using slope formula 
        # : (y2 - y1) / (x2 - x1) to find the third point R that relies on the same
        # elliptic curve E
        slope_lambda = (y2 - y1) / (x2 - x1)

    # else if P are Q are the same point (or only P is given)
    else:
        # calculate the slope of the vertical line L using the implicitly differentiated
        # elliptic curve E formula y^3 = x^2 + Ax + B and the point P
        A = int(E[0]) # const A for curve c
        slope_lambda = (3 * x1**2 + A) / (2 * y1)

    # calculate the third point using the slope and the x, y coordinates of P and Q
    x3 = slope_lambda**2 - x1 - x2
    y3 = slope_lambda * (x1 - x3) - y1

    R_prime = (int(x3), int(-y3)) # get the result R'=(x,-y) reflected across the x-axis given
                        # the new coordinates

    return R_prime # return R'

def is_on_elliptic_curve(P, p, E):
    A = int(E[0])
    B = int(E[1])
    x, y = P
    assert (y*y) % p == (pow(x, 3, p) + A * x + B) % p


def get_elliptic_curve_finite_group(E, p):
    O = (float('inf'), 0) # ideal point
    point_list = [] # set of points in the group E(F_p)

    # const A, B from elliptic curve E equation 
    A = int(E[0]) 
    B = int(E[1])

    # for all possible x's in the range 0...p-1
    for x in range(p):
        for y in range(p): # for all possible y's in the range 0...p-1
            # check if the y satisfies the finite field condition F_p of being a square mod p 
            if (y**2) % p == (x**3 + A*x + B) % p:
                point_list.append((int(x), int(y))) # if so add it to the set

    point_list.append(O) # add the ideal point to the set
    return point_list # return the set


def double_add_algo(n, P, E):
    # check if n is an integer
    assert isinstance(n, int)

    # define the ideal point
    O = (float('inf'), 0)

    # initially set a point Q on the elliptic curve E to be P
    Q = P
    # initially set a point R on the elliptic curve E to be O
    R = O

    # if n is negative, compute -n * P
    if n < 0:
        n = abs(n)
        P = (P[0], -P[1])  # negate the y-coordinate of P

    # while n is greater than 0
    while n:
        # if n is an odd number
        if n % 2 == 1:
            R = elliptic_curve_addition(R, Q, E)  # set R = R (+) Q
        Q = elliptic_curve_addition(Q, Q, E)  # set Q = 2Q or Q = Q (+) Q
        n = math.floor(n/2)  # cut n by half 

    return R  # return the R point

def lenstra_(N):
    A = random.randint(1, N-1) % N
    b = random.randint(1, N-1) % N
    a = random.randint(1, N-1) % N

    P = (a, b)
    B = (b ** 2 - a ** 3 - A * a) % N

    for j in (2, N):
        Q = (j * P) % N
        P = Q
        if Q or P:
            return True
        return P
    return None

