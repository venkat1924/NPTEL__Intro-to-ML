import numpy as np

def get_matrix_input(rows, cols, matrix_name):
    matrix = np.zeros((rows, cols))
    print(f"Enter elements of matrix {matrix_name}:")
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = float(input(f"{matrix_name}[{i + 1}][{j + 1}]: "))
    return matrix

def compute_result_matrix(X, Y):
    T = np.transpose(X)
    TX = np.matmul(T, X)
    inv_TX = np.linalg.inv(TX)
    result_matrix = np.matmul(np.matmul(inv_TX, T), Y)
    return result_matrix

def get_xy_values():
    x = float(input("\nEnter the value for x: "))
    y = float(input("Enter the value for y: "))
    return x, y

if __name__ == "__main__":
    # Input matrix X of order NxP
    N = int(input("Enter the number of rows (N) for matrix X: "))
    P = int(input("Enter the number of columns (P) for matrix X: "))
    X = get_matrix_input(N, P, "X")

    # Input matrix Y of order Nx1
    Y = get_matrix_input(N, 1, "Y")

    # Compute result matrix: inv(T*X) * T * Y
    result_matrix = compute_result_matrix(X, Y)

    # Print the resulting matrix
    print("\nResulting matrix (Px1):")
    for i in range(result_matrix.shape[0]):
        print(f"Result[{i + 1}]: {result_matrix[i][0]}")

    # Get values for x and y
    x, y = get_xy_values()

    # Compute and print the expression Result[0] + x * Result[1] + y * Result[2]
    expression_result = result_matrix[0][0] + x * result_matrix[1][0] + y * result_matrix[2][0]
    print(f"\nResult[0] + x * Result[1] + y * Result[2]: {expression_result}")

