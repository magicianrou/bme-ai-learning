import numpy as np


def main():
    python_list = [1, 2, 3, 4, 5]
    numpy_array = np.array([1, 2, 3, 4, 5])

    print("Python list:")
    print(python_list)

    print("\nNumPy array:")
    print(numpy_array)

    print("\nPython list multiplied by 2:")
    print(python_list * 2)

    print("\nNumPy array multiplied by 2:")
    print(numpy_array * 2)

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print("\nMatrix:")
    print(matrix)

    print("\nMatrix shape:")
    print(matrix.shape)

    print("\nMatrix dtype:")
    print(matrix.dtype)

    print("\nElement at row 0, column 0:")
    print(matrix[0, 0])

    print("\nElement at row 1, column 2:")
    print(matrix[1, 2])

    print("\nFirst row:")
    print(matrix[0, :])

    print("\nSecond column:")
    print(matrix[:, 1])

    print("\nTop-left 2x2 block:")
    print(matrix[0:2, 0:2])


if __name__ == "__main__":
    main()