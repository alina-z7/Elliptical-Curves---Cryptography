from lenstras_elliptical_curve_factorization import ecf

def main():

    input_N = input("Enter a N to be factored (type 'exit' to discontinue): ")
    while input_N != "exit":
        N = int(N)
        res = ecf(N)
        print(res)
    input_N = input("Enter a N to be factored: ")

main()
