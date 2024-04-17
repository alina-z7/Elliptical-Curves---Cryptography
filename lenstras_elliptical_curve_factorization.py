import random
from euclidean_algo import gcd

def ecf(N):
    A = random.randint(1, N-1) % N
    b = random.randint(1, N-1) % N
    a = random.randint(1, N-1) % N

    P = (a, b)
    B = (b ** 2 - a ** 3 - A * a) % N

    for j in (2, N):
        d = gcd(N, j)
        if d > 1:
            if  d < N:
                return d
    return None




