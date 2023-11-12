from lib.PhaseToComplex import PhaseToComplex
from lib.ComplexToPhase import ComplexToPhase
from numpy.linalg import inv as Inverse

def main():
    #I0, I1 e I2
    # I_simetrica = [[-2.08507089], [4.1283552], [-2.04388431]]
    I_simetrica = [[0], [PhaseToComplex(4.1283552, -30)], [PhaseToComplex(-2.04388431, 30)]]

    Ibase = 150000000/138000

    um =(1+0j)
    a = PhaseToComplex(1, 120)
    a2 = PhaseToComplex(1, -120)

    matrix_t = [
        [um, um, um], 
        [um, a2, a], 
        [um, a, a2]
        ]

    # Calculate the inverse of the matrix
    # matrix_t = Inverse(matrix_t)

    result = [0, 0, 0]

    for i in range(len(matrix_t)):
        for j in range(len(I_simetrica[0])):
            for k in range(len(I_simetrica)):
                result[i] += matrix_t[i][k] * I_simetrica[k][j]

    print("\nResult of matrix multiplication:")
    for row in result:
        print(ComplexToPhase(row*Ibase))

if __name__ == "__main__":
    main()