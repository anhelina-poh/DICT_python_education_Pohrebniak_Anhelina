def get_matrix(label=""):
    """
    Description:
    Prompts the user for the dimensions and elements of a matrix.
    Validates that dimensions are positive integers and that each row
    has the correct number of numeric elements.

    Parameters:
    label (str): Optional text to distinguish between 'first' and 'second' matrices.

    Returns:
    list: A 2D list (matrix) containing float values.
    """

    r, c = 0, 0

    while True:
        try:
            print(f"Enter size of {label}matrix: > ", end="")
            dimensions = input().split()

            if len(dimensions) != 2:
                print("Error: Please enter exactly two numbers (rows and columns).")
                continue

            r, c = map(int, dimensions)

            if r <= 0 or c <= 0:
                print("Error: Dimensions must be positive integers greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Matrix dimensions must be integers and positive.")

    print(f"Enter {label}matrix (enter {r} rows, {c} numbers per row):")
    matrix = []
    for i in range(r):
        while True:
            try:
                row_data = input().split()

                if len(row_data) != c:
                    print(f"Error: Expected {c} numbers, but got {len(row_data)}. Please try entering this row again:")
                    continue

                row = [float(x) for x in row_data]
                matrix.append(row)
                break

            except ValueError:
                print("Error: All elements must be valid numbers. Please try entering this row again:")

    return matrix


def format_number(n):
    """Formats numbers to remove trailing zeros or use 2 decimal places.
    Safely handles floating point inaccuracies and negative zeros."""
    if abs(n) < 1e-10:
        return "0"

    if abs(n - round(n)) < 1e-10:
        return str(int(round(n)))

    return f"{n:.2f}"


def print_matrix(matrix):
    """Displays the result matrix or an error if the operation failed."""
    if matrix is None:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        for row in matrix:
            print(*(format_number(x) for x in row))


def add_matrices(a, b):
    """Performs element-wise addition of two matrices of the same size."""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply_by_constant(m, c):
    """Multiplies every element in the matrix by a scalar constant."""
    return [[x * c for x in row] for row in m]


def multiply_matrices(a, b):
    """
    Multiplies two matrices using the dot product of rows and columns.
    Requires: columns of A == rows of B.
    """
    if len(a[0]) != len(b):
        return None
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose_matrix(m, mode):
    """
    Provides four types of matrix transposition:
    1: Main diagonal (rows become columns)
    2: Side diagonal
    3: Vertical reflection
    4: Horizontal reflection
    """
    r, c = len(m), len(m[0])

    if mode == '1':
        return [[m[i][j] for i in range(r)] for j in range(c)]
    elif mode == '2':
        return [[m[i][j] for i in range(r - 1, -1, -1)] for j in range(c - 1, -1, -1)]
    elif mode == '3':
        return [row[::-1] for row in m]
    elif mode == '4':
        return m[::-1]

    return None


def calculate_determinant(m):
    """
    Recursively calculates the determinant of a square matrix
    using Laplace expansion.
    """
    n = len(m)
    if n == 1: return m[0][0]
    if n == 2: return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    res = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in m[1:]]
        res += ((-1) ** j) * m[0][j] * calculate_determinant(minor)
    return res


def calculate_inverse(m):
    """
    Calculates the inverse matrix using the formula: A^-1 = (1/det) * Adj(A).
    Adj(A) is the transpose of the cofactor matrix.
    """
    d = calculate_determinant(m)
    if abs(d) < 1e-10:
        return None

    n = len(m)
    if n == 1: return [[1 / m[0][0]]]

    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = [r[:j] + r[j + 1:] for r_idx, r in enumerate(m) if r_idx != i]
            row.append(((-1) ** (i + j)) * calculate_determinant(minor))
        cofactors.append(row)

    adj = transpose_matrix(cofactors, '1')
    return [[x / d for x in row] for row in adj]


def menu():
    """Interactive loop to handle user choices and input."""
    while True:
        print(
            "\n1. Add matrices\n2. Multiply by constant\n3. Multiply matrices\n4. Transpose\n5. Determinant\n6. Inverse\n0. Exit")
        choice = input("Your choice: > ")

        if choice == "0":
            break

        try:
            if choice == "1":
                print_matrix(add_matrices(get_matrix("first "), get_matrix("second ")))

            elif choice == "2":
                m = get_matrix()
                c = float(input("Enter constant: > "))
                print_matrix(multiply_by_constant(m, c))

            elif choice == "3":
                print_matrix(multiply_matrices(get_matrix("first "), get_matrix("second ")))

            elif choice == "4":
                print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
                t_choice = input("Your choice: > ")
                print_matrix(transpose_matrix(get_matrix(), t_choice))

            elif choice == "5":
                m = get_matrix()
                if len(m) == len(m[0]):
                    print(f"The result is:\n{format_number(calculate_determinant(m))}")
                else:
                    print("Must be square.")

            elif choice == "6":
                m = get_matrix()
                if len(m) != len(m[0]):
                    print("Must be square.")
                else:
                    res = calculate_inverse(m)
                    if res:
                        print_matrix(res)
                    else:
                        print("This matrix doesn't have an inverse.")

        except (ValueError, IndexError, TypeError):
            print("Error in input or sizes.")


if __name__ == "__main__":
    menu()