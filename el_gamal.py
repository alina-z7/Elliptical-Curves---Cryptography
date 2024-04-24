import random
from elliptic_curves import elliptic_curve_addition, get_elliptic_curve_finite_group, double_add_algo

def main():
    # Alice and Bob publicly choose:
    p = 2671
    E = (171, 853)

    P_list = get_elliptic_curve_finite_group(E, p)
    idx = random.randint(1, len(P_list) - 1)
    P = P_list[idx]
    print("Point P on E(F_p):", P)

    # Alice chooses a secret multiplier n_A
    n_A = 1943
    # Computes Q_A = n_A * P
    Q_A = double_add_algo(n_A, P, E)
    print("Alice's public key:", Q_A)

    # Bob's message M
    M_list = get_elliptic_curve_finite_group(E, p)
    idx = random.randint(1, len(M_list) - 1)
    M = M_list[idx]
    print("Bob's message:", M)

    # Random k 1...p
    k = random.randint(1, p)

    # Bob's encryption 
    C1 = double_add_algo(k, P, E)
    point_Q_A_times_k = double_add_algo(k, Q_A, E)
    C2 = elliptic_curve_addition(M, point_Q_A_times_k, E)

    c = (C1, C2)
    print("Ciphertext:", c)

    # Alice's decryption 
    # Compute -n_A * C1
    neg_nA_times_C1 = double_add_algo(-n_A, C1, E)
    # Compute C2 - n_A * C1
    C2_minus_nA_C1 = elliptic_curve_addition(C2, neg_nA_times_C1, E)

    print("Decrypted message:", C2_minus_nA_C1)

main()
