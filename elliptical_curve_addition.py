'''
Elliptical Curve Addition Algorithm - Finding Third Point R' on Common Curve E

Input:
-----
P, Q = points on an elliptic curve E
A = coefficient of the equation E: y^2 = x^3 + Ax + B

Output:
-------
R' = the additive result of P (+) Q

Comments:
---------

'''

def elliptical_curve_addition(P, Q, A):
    O = (float('inf'), 0)
    if P == O:
        return Q
    if Q == O:
        return P
    
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == -y2:
        return O

    if P != Q:
        slope_lambda = (y2 - y1) / (x2 - x1)
    elif P == Q:
        slope_lambda = (3 * x1**2 + A) / (2 * y1)

    x3 = slope_lambda**2 - x1 - x2
    y3 = slope_lambda * (x1 - x3) - y1

    return (x3, -y3)  

P = (7, 16)
Q = (1, 2)
A = -15
print(elliptical_curve_addition(P, Q, A))
